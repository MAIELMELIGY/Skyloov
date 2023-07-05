import os
import threading

from django.shortcuts import render
from PIL import Image

# Create your views here.
from rest_framework import generics, status
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated ,AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product
from .serializers import ProductSerializer

from .models import Cart, CartItem

class ProductSearchView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = Product.objects.all()
        category = self.request.query_params.get("category")
        min_price = self.request.query_params.get("min_price")
        max_price = self.request.query_params.get("max_price")

        if category:
            queryset = queryset.filter(category=category)
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        return queryset


class ProductImageUploadView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, format=None):
        image = request.FILES.get("image")
        product_id = request.data.get("product_id")
        if not product_id:
            return Response(
                {"error": "Product ID is required"}, status=status.HTTP_400_BAD_REQUEST
            )
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response(
                {"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND
            )

        # Validate the image and perform any necessary checks
        # Save the image to the product instance
        product.image = image
        product.save()

        # Perform image processing in a separate thread
        thread = threading.Thread(target=self.process_image, args=(image,))
        thread.start()

        return Response({"message": "Image uploaded successfully"})

    def process_image(self, product):
        # Open the uploaded image using Pillow
        img = Image.open(product.image.path)

        # Generate and save thumbnail
        thumbnail_size = (100, 100)
        thumbnail = img.copy()
        thumbnail.thumbnail(thumbnail_size)
        thumbnail_path = os.path.join(
            "products/", "thumbnails", f"thumbnail_{product.image.name}"
        )
        thumbnail.save(thumbnail_path)

        # Generate and save full-size image
        full_size_path = os.path.join(
            "products/", "full_size", f"full_size_{product.image.name}"
        )
        img.save(full_size_path)

        # Update the product with the processed image paths
        product.thumbnail_image = thumbnail_path
        product.image = full_size_path
        product.save()
class CartView(APIView):
    def get(self, request, format=None):
        cart = self.get_cart(request.user)
        cart_items = cart.items.all()
        # Serialize and return the cart items

    def post(self, request, format=None):
        product_id = request.data.get('product_id')
        quantity = int(request.data.get('quantity', 1))

        product = Product.objects.get(id=product_id)
        cart = self.get_cart(request.user)

        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_item.quantity += quantity
            cart_item.save()

        return Response({'message': 'Product added to cart'})

    def put(self, request, format=None):
        cart_item_id = request.data.get('cart_item_id')
        quantity = int(request.data.get('quantity', 1))

        cart_item = CartItem.objects.get(id=cart_item_id)
        cart_item.quantity = quantity
        cart_item.save()

        return Response({'message': 'Cart item quantity updated'})

    def delete(self, request, format=None):
        cart_item_id = request.data.get('cart_item_id')

        cart_item = CartItem.objects.get(id=cart_item_id)
        cart_item.delete()

        return Response({'message': 'Cart item removed'})

    def get_cart(self, user):
        cart, created = Cart.objects.get_or_create(user=user)
        return cart