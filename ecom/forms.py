from django import forms
from django.forms import widgets
from django.urls import reverse
from .models import *
from paypal.standard.forms import PayPalPaymentsForm
from django.views.generic import FormView

category = forms.ModelMultipleChoiceField(widget=widgets.SelectMultiple(attrs={'size': 30}), queryset=Category.objects.all())

class ProductForm(forms.ModelForm):
  class Meta:
    model = Product
    fields = ['name','category','description','image','price']

class CustomerForm(forms.ModelForm):
  class Meta:
    model  = Customer
    fields = ('photo','actname','country','state','district','address','postalcode','phone','email',)


class CategoryForm(forms.ModelForm):
  class Meta:
    model = Category
    fields = ('categoryname',)
