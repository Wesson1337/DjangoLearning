# Generated by Django 4.0.6 on 2022-07-11 22:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0003_advertisement_price_advertisement_views_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvertisementStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='advertisement',
            name='status',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='advertisement.advertisementstatus'),
        ),
    ]
