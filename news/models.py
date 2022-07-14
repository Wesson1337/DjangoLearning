from django.db import models


class News(models.Model):
    STATUS_CHOICES = [
        ('m', 'Murder'),
        ('g', 'Games'),
        ('t', 'Technologies'),
    ]
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=2000)
    date_added = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)
    activity_flag = models.ForeignKey('ActivityFlag', on_delete=models.CASCADE, related_name='news')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='m')

    def __str__(self):
        return self.title


class ActivityFlag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Comment(models.Model):
    username = models.CharField(max_length=20)
    text = models.CharField(max_length=1000)
    comment_news = models.ForeignKey('News', on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.username
