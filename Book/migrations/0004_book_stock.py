# Generated by Django 5.1.3 on 2024-11-25 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0003_category_category_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='stock',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
