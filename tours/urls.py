from rest_framework.routers import DefaultRouter
from .views import TourViewSet, CategoryViewSet, ReviewViewSet

router = DefaultRouter()
router.register('tours', TourViewSet, basename='tour')
router.register('categories', CategoryViewSet, basename='category')
router.register('reviews', ReviewViewSet, basename='review')

urlpatterns = router.urls