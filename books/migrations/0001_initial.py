# Generated by Django 4.0.6 on 2022-07-26 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('second_name', models.CharField(max_length=255)),
                ('birthdate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('isbn', models.CharField(max_length=100)),
                ('release_year', models.IntegerField(max_length=4)),
                ('pages_amount', models.IntegerField(max_length=10)),
                ('author', models.ManyToManyField(to='books.author')),
            ],
        ),
    ]