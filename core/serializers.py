from django.shortcuts import get_object_or_404
from rest_framework import serializers

from .models import Movie, Review


class MovieSerializer(serializers.ModelSerializer):
    ratings_avg = serializers.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        model = Movie
        fields = ["id", "slug", "title", "description", "ratings_avg"]

    def to_representation(self, instance):
        """
        Changes data representation in movie-list and movie-detail.
        """
        rep = super().to_representation(instance)
        request = self.context.get("request")

        if not request.parser_context.get("kwargs").get("slug"):
            # Remove description from movie-list
            rep.pop("description", None)
        return rep


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["rating"]

    def create(self, validated_data):
        movie_slug = self.context.get("movie_slug")
        user = self.context.get("user")
        movie = get_object_or_404(Movie, slug=movie_slug)
        review = Review.objects.create(movie=movie, user=user, **validated_data)
        self.instance = review
        return review