from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('product/<int:product_id>/update/', views.product_update, name='product_update'),
    path('product/<int:product_id>/delete/', views.product_delete, name='product_delete'),
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
    path('category/<int:category_id>/update/', views.category_update, name='category_update'),
    path('category/<int:category_id>/delete/', views.category_delete, name='category_delete'),
    path('review/<int:review_id>/', views.review_detail, name='review_detail'),
    path('review/<int:review_id>/update/', views.review_update, name='review_update'),
    path('review/<int:review_id>/delete/', views.review_delete, name='review_delete'),
    path('product/create/', views.ProductCreateView.as_view(), name='product_create'),
]
