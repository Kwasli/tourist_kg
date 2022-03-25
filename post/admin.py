from django.contrib import admin

from .models import Category, Post, Comment


# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'author', 'created', 'is_active']
    list_filter = ['created', 'author__username', 'category', 'is_active']
    search_fields = ['title', 'id', 'text', 'created', 'is_active']
    list_editable = ['category', 'is_active']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'id']
    prepopulate_fields = {'slug':('name',)}