from django.contrib import admin
from news.models import News, Comment, ActivityFlag


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(ActivityFlag)
class ActivityFlagAdmin(admin.ModelAdmin):
    pass


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass
