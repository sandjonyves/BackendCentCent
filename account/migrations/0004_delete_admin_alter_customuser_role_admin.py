# Generated by Django 5.0.4 on 2024-10-06 11:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_customuser_email_alter_customuser_date_joined_and_more'),
        ('store', '0006_remove_restaurant_admin'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Admin',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('ETUDIANT', 'étudiant'), ('MARCHAND', 'marchand'), ('ADMIN', 'admin')], default='ETUDIANT', max_length=32),
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.restaurant')),
            ],
            options={
                'verbose_name': 'Administrateur',
                'verbose_name_plural': 'Administrateurs',
            },
            bases=('account.customuser',),
        ),
    ]
