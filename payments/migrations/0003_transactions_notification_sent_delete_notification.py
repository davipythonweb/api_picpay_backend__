# Generated by Django 5.0.7 on 2024-08-16 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='notification_sent',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Notification',
        ),
    ]
