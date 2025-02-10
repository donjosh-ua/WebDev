from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.core import serializers
from django.http import JsonResponse

# Create your views here.

def get_products(request):
    querySet = Product.objects.all().values('id','name','description','quantity')
    data = list(querySet)
    return JsonResponse(data,safe=False)

def get_product(request, id):
    return HttpResponse(f'Producto escogido: {id}')