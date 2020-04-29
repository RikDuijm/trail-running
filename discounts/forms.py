from django import forms
from cart.models import ProductTest


class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductTest
        fields = ('size', 'quantity')
        SIZE_CHOICES = (
                ('', 'Select a size'),
                ('36', '36'),  # First one is the value of select option and second is the displayed value in option
                ('37', '37'),
                ('38', '38'),
                ('39', '39'),
                )
        widgets = {
            'size': forms.Select(choices=SIZE_CHOICES, attrs={'class': 'form-control'}),
        }
