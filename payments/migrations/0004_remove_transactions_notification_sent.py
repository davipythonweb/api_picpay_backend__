# Generated by Django 5.0.7 on 2024-08-16 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_transactions_notification_sent_delete_notification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactions',
            name='notification_sent',
        ),
    ]
