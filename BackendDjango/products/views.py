from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.core import serializers
from django.http import JsonResponse
from django.views import View

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

# Create your views here.

#reduce stock for a product
@csrf_exempt
def patch_products_stock(request,id):
    json_request = json.loads(request.body)
    object = Product.objects.get(id=id)
    object.quantity -= json_request['quantity']
    object.save()
    return HttpResponse('reduced')

#retrieving all products, all information
def get_products(request):
    querySet = Product.objects.all().values()
    data = list(querySet)
    return JsonResponse(data,safe=False)

@csrf_exempt
def post_product(request):
    json_request = json.loads(request.body)
    object = Product(
        name = json_request['name'],
        description = json_request['description'],
        quantity = json_request['quantity'],
    )
    object.save()
    return HttpResponse('created')



@method_decorator(csrf_exempt, name='dispatch') #decorator for allowing put patch methods for testing
class ProductById(View):
    def get_object(self,id):
        model_object = Product.objects.get(id=id)
        object = {
            "id":model_object.id,
            "name":model_object.name,
            "description": model_object.description,
            "quantity":model_object.quantity
        }
        return object
    
    def get(self,request,id):
        data = self.get_object(id)
        return JsonResponse(data) 
    
    def delete(self,request,id): #logical deletion
        pass
    
    def put(self,request,id):
        object = Product.objects.get(id=id)
        json_request = json.loads(request.body)
        object.name = json_request['name']
        object.description = json_request['description']
        object.quantity = json_request['quantity']
        object.save()
        return JsonResponse(self.get_object(id=id))
        
