from django import forms

from .fields import GroupedModelChoiceField
from .models import Product, Size


class SizeForm(forms.Form):
    CHOICES = (
        ('Events', (
            (100, 'Events, no size'),
        )),
        ('Accessories', (
            (101, 'One Size fits all'),
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
            (1, 'XX-Small'),
            (2, 'X-Small'),
            (3, 'Small'),
            (4, 'Medium'),
            (5, 'Large'),
            (6, 'X-Large'),
            (7, 'XX-Large'),
        )),
    )
    size = forms.ChoiceField(choices=CHOICES)



# class SizeModelForm(forms.ModelForm):
#     category = GroupedModelChoiceField(
#         queryset=Size.objects.exclude(parent=None), 
#         choices_groupby='parent'
#     )

#     class Meta:
#         model = Product
#         fields = ('size', 'product_name')