from django.contrib import admin
from .models import Category, Tour, Review

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')

@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'duration_day', 'location')
    list_filter = ('category',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('tour', 'author', 'rating', 'created_at')
    list_filter = ('rating',)