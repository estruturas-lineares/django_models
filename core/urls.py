from django.urls import path
from . import views

urlpatterns = [
    path('', views.index ),
    path('products/', views.products, name= 'products'),
    path('categoryes/', views.categorys, name= 'categoryes'),
    path('supplier/', views.supplier, name= 'supplier' ),
    path('<int:product_id>', views.details)
]
