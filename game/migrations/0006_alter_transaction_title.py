# Generated by Django 3.2.9 on 2021-12-26 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_alter_transaction_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='title',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
