from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('products/', views.products, name= 'products'),
    path('categoryes/', views.categorys, name= 'categoryes'),
    path('supplier/', views.supplier, name= 'supplier' ),
    path('<int:product_id>', views.details),
    path('newproduct/', views.newProduct, name = 'newproduct'),
    path('newcategory/', views.newCategory, name = 'newcategory'),
    path('newsupplier/', views.newSupplier, name = 'newsupplier')
]
