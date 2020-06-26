# Generated by Django 3.0.7 on 2020-06-25 09:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=2000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('rating', models.IntegerField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_review', to=settings.AUTH_USER_MODEL)),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='worker_review', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_cooker', models.BooleanField(default=False)),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('location', models.CharField(blank=True, max_length=50)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('rating', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=2000)),
                ('deadline', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('weight', models.FloatField()),
                ('price', models.IntegerField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customers', to=settings.AUTH_USER_MODEL)),
                ('worker', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='workers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
