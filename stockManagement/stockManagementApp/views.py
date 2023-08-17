from django.shortcuts import render, redirect
from .models import Stock
from .forms import StockCreateForm
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
    context = {
        'title': title,
        'queryset' : queryset,
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