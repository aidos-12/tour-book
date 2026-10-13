from rest_framework import serializers
from .models import Category, Tour, Review


class CategorySerializer(serializers.ModelSerializer):
    tours_count = serializers.IntegerField(source='tours.count', read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'tours_count']


class TourSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Tour
        fields = ['id', 'title', 'description', 'category', 'category_name', 'price', 'duration_day', 'location', 'is_active', 'created_at']
        read_only_fields = ['created_at']

    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError('Название должно содержать не менее 5 символов.')
        return value

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError('Цена должна быть больше нуля.')
        return value

    def validate_duration_day(self, value):
        if value < 1 or value > 60:
            raise serializers.ValidationError('Продолжительность тура должна быть от 1 до 60 дней.')
        return value


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'tour', 'author', 'rating', 'comment', 'created_at']
        read_only_fields = ['id', 'author', 'created_at']

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError('Оценка должна быть от 1 до 5.')
        return value