# Generated by Django 4.0.6 on 2022-07-24 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemNew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='название')),
                ('description', models.TextField(blank=True, verbose_name='описание')),
                ('weight', models.FloatField(verbose_name='вес')),
            ],
        ),
    ]