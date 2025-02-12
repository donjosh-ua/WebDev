from .models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from rest_framework.views import APIView
from rest_framework import status

from django.http import HttpResponse,JsonResponse

# Create your views here.

#reduce stock for a product
@csrf_exempt
@api_view(['PATCH'])
def product_stock(request,id):
    item = Product.objects.get(id=id)
    quantity = json.loads(request.body)['quantity']
    item.quantity -= quantity
    item.save()
    serializable = ProductSerializer(item)
    return Response(serializable.data)

#retrieving all products, all information

#DRF Version
@api_view(['GET'])
def get_products(request):
    items = Product.objects.all()
    serializer =  ProductSerializer(items,many=True)
    return Response(serializer.data)
    


@csrf_exempt
@api_view(['POST'])
def post_product(request):
    serializable = ProductSerializer(data=request.data) #Serialize json to model instance, if valid then save it
    if serializable.is_valid():
        serializable.save()
    return Response(serializable.data)



@method_decorator(csrf_exempt, name='dispatch') #decorator for allowing put patch methods for testing
class ProductById(APIView):
    
    def get_object(self,id):
        return Product.objects.get(id=id)

    def get(self,request,id):
        serializer = ProductSerializer(self.get_object(id))
        return Response(serializer.data) 
    
    def put(self,request,id):
        object = Product.objects.get(id=id)
        serializer = ProductSerializer(object,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
    def delete(self,request,id): #logical deletion
        object = Product.objects.get(id=id)
        object.delete()
        object.save()
        return Response(status=status.HTTP_200_OK)