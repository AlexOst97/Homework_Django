from django import forms
from .models import Product
from django.core.exceptions import ValidationError


class ProductForm(forms.ModelForm):
    ban_words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]

    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price_buy',]

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите наименование'
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите описание'
        })

        self.fields['image'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['category'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['price_buy'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите цену'
        })

    def clean_name(self):
        name = self.cleaned_data.get('name')
        for word in self.ban_words:
            if word in name.lower():
                raise ValidationError(f'Слово "{word}" включен в список запрещенных слов')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        for word in self.ban_words:
            if word in description.lower():
                raise ValidationError(f'Слово "{word}" включен в список запрещенных слов')
        return description

    def clean_price(self):
        price_buy = self.cleaned_data.get('price_buy')
        if price_buy < 0:
            raise ValidationError('Неверно указана цена')
        return price_buy