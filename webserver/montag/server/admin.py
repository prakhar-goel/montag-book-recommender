from django.contrib import admin

from .models import *

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_year', 'publisher')

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'rating')
    pass

@admin.register(Recommender)
class RecommenderAdmin(admin.ModelAdmin):
    list_display = ('version', 'model')
