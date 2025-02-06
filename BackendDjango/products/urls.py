from django.urls import path
from . import views

urlpatterns = [
    path('all/',views.get_products),
    path('id/<int:id>/',views.get_product)
]
