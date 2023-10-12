from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
import csv
from .models import Stock, Categoria
from .forms import StockCreateForm, StockSearchForm, StockUpdateForm, CategoryCreateForm, CategoriaUpdateForm, GastadorForm, CompradorForm
from django.views.generic import TemplateView

# Create your views here.
'''
class HomeView(TemplateView):
    template_name = 'home.html'
'''

def home_view(request):
    template_name = 'home.html'
    title = 'Inicio'
    form = 'Inicio'
    context = {
        'title': title,
        'form' : form,
    }
    return render(request, template_name, context)


def list_items_view(request):
    template_name = 'list_items.html'
    title = 'Listado de Items'
    queryset = Stock.objects.all()
    form = StockSearchForm(request.POST or None)
    if request.method == 'POST':
        queryset = Stock.objects.filter(#categoria__icontains=form['categoria'].value(),
                                        nombre_producto__icontains=form['nombre_producto'].value())
        
        if form['exportar_csv'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="Listado de Productos.csv"'
            writer = csv.writer(response)
            writer.writerow(['Nombre Producto', 'Categoria', 'Cantidad'])
            instance = queryset
            for stock in instance:
                writer.writerow([stock.nombre_producto, stock.categoria, stock.cantidad])
            return response
            
        context = {
            'title': title,
            'queryset' : queryset,
            'form' : form,
            }
    context = {
        'title': title,
        'queryset' : queryset,
        'form' : form,
    }
    return render(request, template_name, context)


def add_items_view(request):
    template_name = 'add_items.html'
    title = 'Agregar Producto'
    form = StockCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, ('Producto agregado exitosamente'))
        return redirect('list_items')
    context = {
        'title': title,
        'form' : form,
    }
    return render(request, template_name, context)


def update_items_view(request, pk):
    template_name = 'add_items.html'
    title = 'Actualizar Producto'
    queryset = Stock.objects.get(id=pk)
    form = StockUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = StockUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, ('Producto actualizado exitosamente'))
            return redirect('/list_items')

    context = {
        'title': title,
        'form' : form,
    }
    return render(request, template_name, context)


def delete_items_view(request, pk):
    queryset = Stock.objects.get(id=pk)
    template_name = 'delete_items.html'
    title = 'Borrar Producto - '+queryset.nombre_producto
    if request.method == 'POST':
        queryset.delete()
        messages.success(request, ('Producto borrado exitosamente'))
        return redirect('/list_items')

    context = {
        'title': title,
        'nombre_producto': queryset.nombre_producto
    }
    return render(request, template_name, context)


def list_categories_view(request):
    template_name = 'list_categories.html'
    title = 'Listado de Categorias'
    queryset = Categoria.objects.all()

    context = {
        'title': title,
        'queryset' : queryset,
    }
    return render(request, template_name, context)


def add_categories_view(request):
    template_name = 'add_items.html'
    title = 'Agregar Categoría'
    form = CategoryCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, ('Categoría agregada exitosamente'))
        return redirect('add_items')
    context = {
        'title': title,
        'form' : form,
    }
    return render(request, template_name, context)


def update_categories_view(request, pk):
    template_name = 'add_items.html'
    title = 'Actualizar Categoría'
    queryset = Categoria.objects.get(id=pk)
    form = CategoriaUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = CategoriaUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, ('Categoría actualizada exitosamente'))
            return redirect('/list_items')

    context = {
        'title': title,
        'form' : form,
    }
    return render(request, template_name, context)


def delete_categories_view(request, pk):
    queryset = Categoria.objects.get(id=pk)
    template_name = 'delete_categories.html'
    title = 'Borrar Categoría - '+queryset.nombre
    if request.method == 'POST':
        queryset.delete()
        messages.success(request, ('Categoría borrado exitosamente'))
        return redirect('/list_items')

    context = {
        'title': title,
        'nombre_cat': queryset.nombre
    }
    return render(request, template_name, context)


def item_detail_view(request, pk):
    template_name = 'item_detail.html'
    title = 'Detalle de Producto - '+Stock.objects.get(id=pk).nombre_producto
    queryset = Stock.objects.get(id=pk)

    context = {
        'title': title,
        'queryset' : queryset,
    }
    return render(request, template_name, context)


def items_gastados_view (request, pk):
    template_name = 'add_items.html'
    title = 'Gastar Producto' + str(Stock.objects.get(id=pk).nombre_producto)
    queryset = Stock.objects.get(id=pk)
    form = GastadorForm(request.POST or None, instance=queryset)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.cantidad = instance.cantidad - instance.cantidad_gastada
        #instance.gastado_por = str(request.user)
        messages.success(request, ('Gastado exitosamente ' + str(instance.cantidad_gastada) + ' ' + str(instance.etiqueta) + ' del producto ' + str(instance.nombre_producto) + '. Restantes: ' + str(instance.cantidad) + ' ' + str(instance.etiqueta)))
        instance.save()
        return redirect('/detail_item/'+str(instance.id))
        #return HttpResponse (instance.get_absolute_url())

    context = {
        'title': title,
        'queryset' : queryset,
        'form' : form,
        'username' : 'Gastado por ' + str(request.user),
    }
    return render(request, template_name, context)


def items_comprados_view (request, pk):
    template_name = 'add_items.html'
    title = 'Comprar Producto' + str(Stock.objects.get(id=pk).nombre_producto)
    queryset = Stock.objects.get(id=pk)
    form = CompradorForm(request.POST or None, instance=queryset)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.cantidad = instance.cantidad + instance.cantidad_comprada
        instance.save()
        #instance.comprado_por = str(request.user)
        messages.success(request, ('Comprado exitosamente ' + str(instance.cantidad_comprada) + ' ' + str(instance.etiqueta) + ' del producto ' + str(instance.nombre_producto) + '. En stock: ' + str(instance.cantidad) + ' ' + str(instance.etiqueta)))
        return redirect('/detail_item/'+str(instance.id))
        #return HttpResponse (instance.get_absolute_url())

    context = {
        'title': title,
        'queryset' : queryset, #instance
        'form' : form,
        'username' : 'Comprado por ' + str(request.user),
    }
    return render(request, template_name, context)