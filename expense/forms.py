from django import forms
from .models import Book

class UploadFileForm(forms.Form):
    file = forms.FileField()

    # class Meta:
    #     model = Book
    #     fields = ('file')