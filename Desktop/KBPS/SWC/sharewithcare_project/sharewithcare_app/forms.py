from django import forms
from django.forms import ModelForm, models

from .models import Add, Add2, Add3, pay, List


class AddForm(ModelForm):
    class Meta:
        model = Add
        fields = [
            'rawname', 'quantity', 'image'
        ]

class AddCategory(ModelForm):
    class Meta:
        model = List
        fields = [
            'categoryname', 'numberofvarieties', 'collage'
        ]

class Add2Form(ModelForm):
    class Meta:
        model = Add2
        fields = [
            'intername', 'quantity', 'image'
        ]

class Add3Form(ModelForm):
    class Meta:
        model = Add3
        fields = [
            'endname', 'brandname', 'quantity', 'price', 'image'
        ]

class pay(ModelForm):
    class Meta:
        model = pay
        password = forms.CharField(widget=forms.PasswordInput)
        fields = [
            'username', 'password', 'amount'
        ]
        widgets = {
            'password': forms.PasswordInput(),
        }
