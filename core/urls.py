from django.urls import path
from . import views

urlpatterns = [
    path('', views.index.as_view(), name = 'index'),
    path('products/', views.products.as_view(), name= 'products'),
    path('categoryes/', views.categorys.as_view(), name= 'categoryes'),
    path('supplier/', views.supplier.as_view(), name= 'supplier' ),
    path('<int:pk>', views.details.as_view(), name = 'product-detail'),
    path('newproduct/', views.newProduct.as_view(), name = 'newproduct'),
    path('newcategory/', views.newCategory.as_view(), name = 'newcategory'),
    path('newsupplier/', views.newSupplier.as_view(), name = 'newsupplier')
]
