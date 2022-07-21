# Generated by Django 4.0.6 on 2022-07-19 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('code', models.CharField(max_length=100, verbose_name='code')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='price')),
            ],
        ),
    ]