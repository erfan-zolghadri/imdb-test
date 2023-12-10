from django.contrib import admin

from .models import Movie, Review


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ["pk", "title", "release_date", "is_active", "created_at"]
    list_display_links = ["pk", "title"]
    list_editable = ["is_active"]
    list_filter = ["is_active", "created_at"]
    list_per_page = 10
    prepopulated_fields = {"slug": ["title"]}
    readonly_fields = ["created_at", "updated_at"]
    search_fields = ["title"]
    ordering = ["-created_at"]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["movie", "rating", "user", "created_at"]
    list_filter = ["created_at"]
    list_per_page = 10
    readonly_fields = ["created_at"]
    search_fields = ["movie__title"]
    ordering = ["-created_at"]
