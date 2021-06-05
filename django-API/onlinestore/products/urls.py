from django.urls import path
from .views import product_list,product_detail,manufacturer_list,manufacturer_detail


urlpatterns = [
    path("products/",product_list,name="product_list"),
    path("products/<int:pk>/",product_detail,name="product_detail"),

    path("manufacturers/",manufacturer_list,name="manufacturer_list")

]
