# Generated by Django 5.1.4 on 2025-01-01 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0004_alter_book_subtitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='subtitle',
            field=models.CharField(default='', max_length=350, null=True),
        ),
    ]