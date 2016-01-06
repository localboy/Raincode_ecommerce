from django import forms
from django.forms.models import modelformset_factory
from .models import Variation

class VariationInventoryFormSet(forms.ModelForm):
    class Meta:
        model = Variation
        fields = [
            "title",
            "price",
            "sale_price",
            "inventory",
            "active"
        ]

VariationInventoryFormSet = modelformset_factory(Variation, form=VariationInventoryFormSet, extra=1)