from rest_framework import generics
from .models import Tour, Category
from .serializers import TourSerializer, CategorySerializer

class TourListCreateAPIView(generics.ListCreateAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer

class TourDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer

class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TourByCategoryListAPIView(generics.ListAPIView):
    serializer_class = TourSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Tour.objects.filter(category_id=category_id, is_active=True)