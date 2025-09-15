from django import forms

from online_shop.models import Category


class AddCategoryForm(forms.Form):
    title = forms.CharField(label='Название', max_length=100)


class AddProductForm(forms.Form):
    title = forms.CharField(label="Название", max_length=100)
    price = forms.DecimalField(label="Цена", max_digits=5, decimal_places=2)
    description = forms.CharField(widget=forms.Textarea, label="Описание")
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория')