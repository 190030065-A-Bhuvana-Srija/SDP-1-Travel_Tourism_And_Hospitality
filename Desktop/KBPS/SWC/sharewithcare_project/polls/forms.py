from django import forms
from .models import seller

class sellerform(forms.ModelForm):
    class Meta:
        model=seller
        fields= ('user_name','crop_name','price_per_kg','max_kg','photo')