from django import forms
from django.forms import widgets
from .models import *

category = forms.ModelMultipleChoiceField(widget=widgets.SelectMultiple(attrs={'size': 30}), queryset=Category.objects.all())

class ProductForm(forms.ModelForm):
  class Meta:
    model = Product
    fields = ['name','category','description','image','price']

class CustomerForm(forms.ModelForm):
  class Meta:
    model  = Customer
    fields = ('photo','phone','email',)


class CategoryForm(forms.ModelForm):
  class Meta:
    model = Category
    fields = ('categoryname',)