from django import forms

from .fields import GroupedModelChoiceField
from .models import Product, Item


class SizeForm(forms.Form):
    CHOICES = (
        ('Events', (
            (11, 'Events'),
        )),
        ('Accessories', (
            (21, 'One Size'),
        )),
        ('Shoes', (
            (36, '36'),
            (37, '37'),
            (38, '38'),
            (39, '39'),
            (40, '40'),
            (41, '41'),                        
            (42, '42'),
            (43, '43'),
            (44, '44'),
            (45, '45'),
            (46, '46'),
            (47, '47'),                                
        )),
        ('Clothes', (
            (51, 'XX-Small'),
            (61, 'X-Small'),
            (62, 'Small'),
            (63, 'Medium'),
            (64, 'Large'),
            (65, 'X-Large'),
            (66, 'XX-Large'),
        )),
    )
    size = forms.ChoiceField(choices=CHOICES)


class SizeModelForm(forms.ModelForm):
    size = GroupedModelChoiceField(queryset=Item.objects.exclude(parent=None), choices_groupby='parent')

    class Meta:
        model = Product
        fields = ('size')
