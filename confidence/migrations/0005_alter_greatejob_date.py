# Generated by Django 3.2.9 on 2022-01-05 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('confidence', '0004_alter_greatejob_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='greatejob',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
