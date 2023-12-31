from django import forms
from .models import Stock, Categoria
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, HTML, Field, Row

class StockCreateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['categoria', 'nombre_producto', 'cantidad', 'etiqueta', 'fecha_caducidad']

        widgets = {
            'fecha_caducidad': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'class': 'form-control datepicker', 
                        'placeholder': 'Selecciona la fecha',
                        'type': 'date'
                    }),
        }

    def __init__(self, *args, **kwargs):
        super(StockCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False # No incluir <form></form>
        self.helper.layout = Layout(
            Div(
                Div(Field('nombre_producto'), css_class="col-6"),
                Div(Field('categoria'), css_class="col-6"),
                css_class="row"
            ),
            Row( #De esta forma no tendremos que usar la clase row
                Div(Field('cantidad'), css_class="col-3"),
                Div(Field('etiqueta'), css_class="col-5"),
                Div(Field('fecha_caducidad'), css_class="col-4"),
                css_class="row"
            )
        )

    def clean_nombre_producto(self):
        nombre_producto = self.cleaned_data.get('nombre_producto')
        if not nombre_producto:
            raise forms.ValidationError('Este campo es obligatorio')
        
        for instance in Stock.objects.all():
            if nombre_producto == instance.nombre_producto:
                raise forms.ValidationError('Este producto ya existe')
        return nombre_producto

    def clean_categoria(self):
        categoria = self.cleaned_data.get('categoria')
        if not categoria:
            raise forms.ValidationError('Este campo es obligatorio')
        
        #TODO Descomentar cuando esté acabado y sea un dropdown
        #for instance in Stock.objects.all():
        #    if categoria == instance.categoria:
        #        raise forms.ValidationError('Esta categoria ya existe')
        return categoria


class StockSearchForm(forms.ModelForm):
    exportar_csv = forms.BooleanField(required=False)
    class Meta:
        model = Stock
        fields = ['categoria', 'nombre_producto']
        
    def __init__(self, *args, **kwargs):
        super(StockSearchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False # No incluir <form></form>
        self.helper.layout = Layout(
            Div(
                Field('nombre_producto')
            ),
            Div(
                Field('categoria')
            ),
            Div(
                Field('exportar_csv')
            ),
        )


class StockUpdateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['categoria', 'nombre_producto', 'cantidad', 'etiqueta', 'fecha_caducidad']
        
    def __init__(self, *args, **kwargs):
        super(StockUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False # No incluir <form></form>
        self.helper.layout = Layout(
            Div(
                Div(Field('nombre_producto'), css_class="col-6"),
                Div(Field('categoria'), css_class="col-6"),
                css_class="row"
            ),
            Row( #De esta forma no tendremos que usar la clase row
                Div(Field('cantidad'), css_class="col-3"),
                Div(Field('etiqueta'), css_class="col-5"),
                Div(Field('fecha_caducidad'), css_class="col-4"),
                css_class="row"
            )
        )


class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']
        
    def __init__(self, *args, **kwargs):
        super(CategoryCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False # No incluir <form></form>
        self.helper.layout = Layout(
            Div(
                Div(Field('nombre'), css_class="col-6"),
                css_class="row"
            )
        )

    def clean_categoria(self):
        categoria = self.cleaned_data.get('categoria')
        if not categoria:
            raise forms.ValidationError('Este campo es obligatorio')
        
        #TODO Descomentar cuando esté acabado y sea un dropdown
        for instance in Stock.objects.all():
            if categoria == instance.categoria:
                raise forms.ValidationError('Esta categoria ya existe')
        return categoria


class CategoriaUpdateForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']
        
    def __init__(self, *args, **kwargs):
        super(CategoriaUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False # No incluir <form></form>
        self.helper.layout = Layout(
            Div(
                Div(Field('nombre'), css_class="col-6"),
                css_class="row"
            )
        )

class GastadorForm (forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['cantidad_gastada', 'gastado_por']
        
    def __init__(self, *args, **kwargs):
        super(GastadorForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False # No incluir <form></form>
        self.helper.layout = Layout(
            Div(
                Div(Field('cantidad_gastada'), css_class="col-6"),
                Div(Field('gastado_por'), css_class="col-6"),
                css_class="row"
            )
        )

class CompradorForm (forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['cantidad_comprada', 'comprador', 'proveedor', 'precio']
        
    def __init__(self, *args, **kwargs):
        super(CompradorForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False # No incluir <form></form>
        self.helper.layout = Layout(
            Div(
                Div(Field('cantidad_comprada'), css_class="col-3"),
                Div(Field('comprador'), css_class="col-9"),
                css_class="row"
            ),
            Div(
                Div(Field('proveedor'), css_class="col-9"),
                Div(Field('precio'), css_class="col-3"),
                css_class="row"
            )
        )