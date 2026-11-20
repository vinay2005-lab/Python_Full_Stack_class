from django.contrib import admin
from .models import Movie, Review


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "genre","release_date")
    search_fields = ("title",)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("movie", "user", "rating", "created_at")
    list_filter = ("rating",)
