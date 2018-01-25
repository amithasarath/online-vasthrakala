from django import forms
from . models import ItemGroup,ItemStock


class ItemGroupForm(forms.ModelForm):
    class Meta:
        model = ItemGroup
        fields = "__all__"

class ItemStockForm(forms.ModelForm):
    class Meta:
        model = ItemStock
        fields = "__all__"