from django.urls import path
from .views import TourListCreateAPIView, TourDetailAPIView, CategoryListCreateAPIView, CategoryDetailAPIView, TourByCategoryListAPIView

urlpatterns = [
    path('tours/', TourListCreateAPIView.as_view(), name='tour-list'),
    path('tours/<int:pk>/', TourDetailAPIView.as_view(), name='tour-detail'),
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view(), name='category-detail'),
    path('categories/<int:category_id>/tours/', TourByCategoryListAPIView.as_view(), name='tour-by-category'),
]