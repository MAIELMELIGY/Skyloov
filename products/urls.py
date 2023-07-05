from django.urls import path
from .views import ProductSearchView,ProductImageUploadView,CartView


urlpatterns = [
    path('search/', ProductSearchView.as_view(), name='search'),
    path('upload-image/', ProductImageUploadView.as_view(), name='upload-image'),
    path('cart/', CartView.as_view(), name='cart'),


]