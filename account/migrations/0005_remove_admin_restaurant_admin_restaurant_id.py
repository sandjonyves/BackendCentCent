# Generated by Django 5.0.4 on 2024-10-06 11:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_delete_admin_alter_customuser_role_admin'),
        ('store', '0006_remove_restaurant_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin',
            name='restaurant',
        ),
        migrations.AddField(
            model_name='admin',
            name='restaurant_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.restaurant'),
        ),
    ]
