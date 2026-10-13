from django.db.models import Count
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .models import Tour, Category, Review
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import TourSerializer, CategorySerializer, ReviewSerializer


class TourViewSet(viewsets.ModelViewSet):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        queryset = Tour.objects.select_related('category')
        if self.request.user.is_staff:
            return queryset
        return queryset.filter(is_active=True)

    @action(detail=True, methods=['post'], permission_classes=[IsAdminUser])
    def deactivate(self, request, pk=None):
        tour = self.get_object()
        tour.is_active = False
        tour.save()
        return Response({'status': 'deactivated'})


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]

    @action(detail=True, methods=['get'])
    def tours(self, request, pk=None):
        category = self.get_object()
        tours = category.tours.filter(is_active=True)
        serializer = TourSerializer(tours, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def popular(self, request):
        categories = Category.objects.annotate(n=Count('tours')).order_by('-n')[:3]
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.select_related('tour', 'author').all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)