from django.contrib import admin
from django.db.models import QuerySet

from news.models import News, Comment, ActivityFlag


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'username']


@admin.register(ActivityFlag)
class ActivityFlagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):

    actions = ['mark_as_murder', 'mark_as_games', 'mark_as_technologies']

    def mark_as_murder(self, request, queryset: QuerySet):
        queryset.update(status='m')

    def mark_as_games(self, request, queryset: QuerySet):
        queryset.update(status='g')

    def mark_as_technologies(self, request, queryset: QuerySet):
        queryset.update(status='t')

    mark_as_games.short_desription = 'Присвоить статус "Игры"'
    mark_as_murder.short_desription = 'Присвоить статус "Убийство"'
    mark_as_technologies.short_desription = 'Присвоить статус "Технологии"'
    list_display = ['id', 'title', 'activity_flag']
    list_filter = ['activity_flag', 'title']
    search_fields = ['title', 'content']
    fieldsets = (
        ('Основные сведения', {
            'fields': ('title', 'content'),
            'classes': ['collapse']
        }),
        ('Доп.поля', {
            'fields': ('activity_flag', 'activity_flag2'),
            'classes': ['collapse']
        })
    )
