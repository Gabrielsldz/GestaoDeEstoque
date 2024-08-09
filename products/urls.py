from django.urls import path
from . import views


urlpatterns = [
    path('products/list/', views.ProductListView.as_view(), name='product_list'),
    path('products/create/', views.ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/detail/', views.ProductDetailView.as_view(), name='product_detail'),
    path('products/<int:pk>/update/', views.ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),

    path('api/v1/products/', views.ProductCreateListAPIView.as_view(), name='product-create-list-api-view'),
    path('api/v1/products/<int:pk>/', views.ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-detail-api-view'),
]
