# Generated by Django 3.1.4 on 2021-01-26 08:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auto_20210126_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlist',
            name='categories',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='auctions.categories'),
        ),
        migrations.AlterField(
            model_name='auctionlist',
            name='winner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
