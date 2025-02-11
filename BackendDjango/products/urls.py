from django.urls import path
from . import views

urlpatterns = [
    path('all/',views.get_products),
    path('id/<int:id>/',views.ProductById.as_view()), #Product getter depending on meth
    path('',views.post_product),
    path('id/<int:id>/stock/', views.patch_products_stock)
]
