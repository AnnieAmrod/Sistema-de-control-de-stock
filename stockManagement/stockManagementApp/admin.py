from django.contrib import admin
from .forms import StockCreateForm

# Register your models here.
from .models import Stock


class StockCreateAdmin(admin.ModelAdmin):
    list_display = ['nombre_producto', 'categoria', 'cantidad', 'etiqueta']
    form = StockCreateForm
    list_filter = ['categoria']
    search_fields = ['categoria', 'nombre_producto']

admin.site.register(Stock, StockCreateAdmin)