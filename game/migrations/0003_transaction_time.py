# Generated by Django 3.2.9 on 2021-12-26 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_alter_transaction_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='time',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
    ]
