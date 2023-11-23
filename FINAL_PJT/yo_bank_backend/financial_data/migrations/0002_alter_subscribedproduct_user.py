# Generated by Django 4.2.4 on 2023-11-23 15:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('financial_data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribedproduct',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subbb', to=settings.AUTH_USER_MODEL),
        ),
    ]