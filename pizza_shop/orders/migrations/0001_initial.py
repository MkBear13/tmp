# Generated by Django 5.1.2 on 2024-10-13 18:10

import django.db.models.deletion
import orders.validators
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, null=True)),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('age', models.PositiveIntegerField(null=True, validators=[orders.validators.users_age_validator])),
                ('sex', models.CharField(choices=[('m', 'male'), ('f', 'female')], max_length=1, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('processing', 'Processing'), ('completed', 'Completed')], default='pending', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('pizza', 'Pizza'), ('snack', 'Snack'), ('drink', 'Drink')], max_length=5)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('ingredients', models.TextField()),
                ('nutrition', models.JSONField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='orders.user')),
                ('admin_rate', models.IntegerField(null=True)),
            ],
            bases=('orders.user',),
        ),
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='orders.user')),
                ('byer_email', models.EmailField(max_length=254, null=True)),
            ],
            bases=('orders.user',),
        ),
        migrations.AddIndex(
            model_name='user',
            index=models.Index(fields=['first_name'], name='first_name_index'),
        ),
        migrations.AddIndex(
            model_name='user',
            index=models.Index(fields=['last_name'], name='last_name_index'),
        ),
        migrations.AddIndex(
            model_name='user',
            index=models.Index(fields=['age'], name='age_index'),
        ),
        migrations.AddIndex(
            model_name='user',
            index=models.Index(fields=['sex'], name='sex_index'),
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='orders.product'),
        ),
    ]
