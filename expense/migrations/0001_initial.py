# Generated by Django 5.1.4 on 2024-12-31 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField()),
                ('title', models.CharField(max_length=350)),
                ('subtitle', models.CharField(max_length=350)),
                ('author', models.CharField(max_length=100)),
                ('publisher', models.CharField(max_length=100)),
                ('published_date', models.DateField()),
                ('category', models.CharField(choices=[('Business Analytics', 'Business Analytics'), ('Python', 'Python'), ('Data Science', 'Data Science'), ('Math', 'Math')], max_length=100)),
                ('distribution_expense', models.FloatField()),
            ],
        ),
    ]