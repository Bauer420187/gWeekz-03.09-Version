from django.forms import ModelForm
from accounts.models import Product, Video
from django import forms


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"



class Video_form(forms.ModelForm):
    class Meta:
        model=Video
        fields=("caption","video")
