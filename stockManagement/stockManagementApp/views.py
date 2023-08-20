from django.shortcuts import render, redirect
from .models import Stock
from .forms import StockCreateForm, StockSearchForm, StockUpdateForm
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
    title = 'Agregar Items'
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
    title = 'Actualizar Items'
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