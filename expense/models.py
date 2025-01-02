from datetime import datetime
from django.contrib.auth.models import User

from django.db import models

# Create your models here.
class Book(models.Model):
    """
    Model for book category
    """
    BOOK_CATEGORY = (
        ('Business Analytics', 'Business Analytics'),
        ('deep learning', 'deep learning'),
        ('Python', 'python'),
        ('Data Science', 'data science'),
        ('Maths', 'maths'),
        ('Data ethics', 'Data ethics'),
        ('NLP', 'NLP'),
        ('R Studio', 'R Studio'),
        ('SQL', 'SQL'),
        ('statistics', 'statistics'),
        ('visualization', 'visualization'),

    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uid = models.CharField(max_length=100)
    title = models.CharField(max_length=350)
    subtitle = models.CharField(max_length=350, default='', null=True)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    published_date = models.CharField(max_length=20)
    category = models.CharField(max_length=100, choices=BOOK_CATEGORY, null=True)
    distribution_expense = models.FloatField()

    def __str__(self):
        return self.publisher
    
class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.file.name