from django.shortcuts import render, redirect
from .models import Stock, Categoria
from .forms import StockCreateForm, StockSearchForm, StockUpdateForm, CategoryCreateForm, CategoriaUpdateForm
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
        queryset = Stock.objects.filter(categoria__icontains=form['categoria'].value(),
                                        nombre_producto__icontains=form['nombre_producto'].value())
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
        return redirect('/list_items')

    context = {
        'title': title,
        'nombre_cat': queryset.nombre
    }
    return render(request, template_name, context)
    