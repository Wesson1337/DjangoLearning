from django.contrib import admin

from blog.models import Blog, Post, Author


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']