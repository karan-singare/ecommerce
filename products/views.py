from django.http import Http404
from django.views.generic.list import ListView
from django.views.generic.detail import  DetailView
from django.shortcuts import render, get_object_or_404

from .models import Product

# Create your views here.

# class based view
class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'products/list.html'

    # The default context can be accessed in view using 'object_list'

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context

# function based view
def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'products/list.html', context=context)

class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'products/detail.html'

    # The default context can be accessed in view using 'object'

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context

def product_detail_view(request, pk=None, *args, **kwargs):
    # instance = Product.objects.get(pk=pk)
    # instance = get_object_or_404(Product, pk=pk)

    # try:
    #     instance = Product.objects.get(id=pk)
    # except Product.DoesNotExist:
    #     print('No such product')
    #     raise Http404('Product doesn\'t exists medthod1')
    # except:
    #     print('huh?')

    qs = Product.objects.filter(id=pk)
    if qs.exists() and qs.count() == 1:
        instance = qs.first()
    else:
        raise Http404("Product doesn't exists method 2")

    context = {
        'object': instance
    }
    return render(request, 'products/detail.html', context=context)
