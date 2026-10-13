from django.contrib import admin
from .models import Category, Tour, Review


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    search_fields = ['name']


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'price', 'is_active']
    list_filter = ['is_active', 'category']
    search_fields = ['title', 'location']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'tour', 'author', 'rating', 'created_at']
    list_filter = ['rating', 'created_at']
    search_fields = ['author__username', 'comment']