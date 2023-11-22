from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Product, User

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('id','name','image','description',)

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)