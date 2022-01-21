from django import forms
from .models import *

class SearchForm(forms.ModelForm):
   class Meta:
     model = Product
     fields = ['name', 'category']