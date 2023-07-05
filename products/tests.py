# from django.test import TestCase
# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APIClient
# from.models import Product
# from.serializers import ProductSerializer
# from.views import ProductSearchView
# from django.test import TestCase
# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APIClient
# from.models import Product
# from.serializers import ProductSerializer
# from.views import ProductSearchView

# class ProductSearchViewTestCase(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.product1 = Product.objects.create(name='Product 1', min_price=10.0 , max_price=50.0)
#         self.product2 = Product.objects.create(name='Product 2', min_price=10.0 , max_price=50.0)
#         self.product3 = Product.objects.create(name='Product 3', min_price=10.0 , max_price=50.0)

#     # def test_get_queryset_no_filters(self):
#     #     url = reverse('search')
#     #     response = self.client.get(url)
#     #     self.assertEqual(response.status_code, status.HTTP_200_OK)
#     #     print("zzzzzzzzzzzzzzzzzzzz",len(response.data))
#     #     print("bbbbbbbbbbbbbbbbbbbbbb",(response.data).count())
#     #     self.assertEqual((response.data).count(), 3)
#     def test_get_queryset_category_filter(self):
#         url = reverse('search') + '?category=1'
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), 1)
#         self.assertEqual(response.data[0]['name'], 'Product 1')

# #     def test_get_queryset_min_price_filter(self):
# #         url = reverse('search/') + '?min_price=20.0'
# #         response = self.client.get(url)
# #         self.assertEqual(response.status_code, status.HTTP_200_OK)
# #         self.assertEqual(len(response.data), 2)
# #         self.assertEqual(response.data[0]['name'], 'Product 2')
# #         self.assertEqual(response.data[1]['name'], 'Product 3')

# #     def test_get_queryset_max_price_filter(self):
# #         url = reverse('search/') + '?max_price=20.0'
# #         response = self.client.get(url)
# #         self.assertEqual(response.status_code, status.HTTP_200_OK)
# #         self.assertEqual(len(response.data), 2)
# #         self.assertEqual(response.data[0]['name'], 'Product 1')
# #         self.assertEqual(response.data[1]['name'], 'Product 2')

# #     def test_get_queryset_multiple_filters(self):
# #         url = reverse('search/') + '?category=1&min_price=20.0'
# #         response = self.client.get(url)
# #         self.assertEqual(response.status_code, status.HTTP_200_OK)
# #         self.assertEqual(len(response.data), 1)
# #         self.assertEqual(response.data[0]['name'], 'Product 2')

# #     def test_get_queryset_invalid_filter(self):
# #         url = reverse('search/') + '?invalid_filter=1'
# #         response = self.client.get(url)
# #         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

# #     def test_search_by_category_and_min_price(self):
# #         url = reverse('product-search')
# #         response = self.client.get(url, {'category': '1', 'in_price': 20})
# #         self.assertEqual(response.status_code, status.HTTP_200_OK)
# #         expected_data = ProductSerializer([self.product3], many=True).data
# #         self.assertEqual(response.data, expected_data)
        
# # class ProductImageUploadViewTestCase(TestCase):
# #     def setUp(self):
# #         self.client = APIClient()
# #         self.user = User.objects.create_user(
# #             username='testuser',
# #             password='testpass'
# #         )
# #         self.client.force_authenticate(user=self.user)
# #         self.product = Product.objects.create(
# #             name='Test Product',
# #             description='Test description',
# #             price=10.00,
# #             image=SimpleUploadedFile(
# #                 name='test_image.jpg',
# #                 content=open('test_image.jpg', 'rb').read(),
# #                 content_type='image/jpeg'
# #             )
# #         )

# #     def test_upload_image_success(self):
# #         url = reverse('product-image-upload')
# #         data = {
# #             'product_id': self.product.id,
# #             'image': SimpleUploadedFile(
# #                 name='test_image.jpg',
# #                 content=open('test_image.jpg', 'rb').read(),
# #                 content_type='image/jpeg'
# #             )
# #         }
# #         response = self.client.post(url, data, format='multipart')
# #         self.assertEqual(response.status_code, status.HTTP_200_OK)
# #         self.assertEqual(response.data['message'], 'Image uploaded successfully')
# #         self.product.refresh_from_db()
# #         self.assertTrue(self.product.image)
# #         self.assertTrue(self.product.thumbnail_image)
# #         self.assertTrue(self.product.full_size_image)

# #     def test_upload_image_missing_product_id(self):
# #         url = reverse('product-image-upload')
# #         data = {
# #             'image': SimpleUploadedFile(
# #                 name='test_image.jpg',
# #                 content=open('test_image.jpg', 'rb').read(),
# #                 content_type='image/jpeg'
# #             )
# #         }
# #         response = self.client.post(url, data, format='multipart')
# #         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
# #         self.assertEqual(response.data['error'], 'Product ID is required')

# #     def test_upload_image_product_not_found(self):
# #         url = reverse('product-image-upload')
# #         data = {
# #             'product_id': 100,
# #             'image': SimpleUploadedFile(
# #                 name='test_image.jpg',
# #                 content=open('test_image.jpg', 'rb').read(),
# #                 content_type='image/jpeg'
# #             )
# #         }
# #         response = self.client.post(url, data, format='multipart')
# #         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
# #         self.assertEqual(response.data['error'], 'Product not found')