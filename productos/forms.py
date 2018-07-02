from django import forms
from .models import Producto, Categoria, Log
from django.forms import ModelForm, Textarea, DateInput, NumberInput, SelectDateWidget

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'descripcion': Textarea(attrs={'cols': 40, 'rows': 15})
        }

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class VentaForm(ModelForm):
    class Meta:
        model = Log
        fields = '__all__'
        widgets = {
        	'fecha': SelectDateWidget(),
            'cantidad_vendida': NumberInput(attrs={'value': 0})
        }
