# Generated by Django 4.0.6 on 2022-07-28 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_author_alter_blog_name_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ManyToManyField(related_name='authors', to='blog.author'),
        ),
    ]
