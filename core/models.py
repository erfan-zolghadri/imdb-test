from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class ActiveMovieManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class Movie(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    release_date = models.DateField()
    is_active = models.BooleanField(default=True, verbose_name="active")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    objects = models.Manager()
    active_movies = ActiveMovieManager()


class Review(models.Model):
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name="reviews"
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "movie"],
                name="unique_review",
            )
        ]
