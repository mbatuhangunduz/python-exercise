from django.urls import path
from .views import (
    # dynamic_lookup_view,
    render_initial_data,
    product_detail_view,
    product_create_view,
    product_delete_view,
    product_list_view
)

app_name = "products"
urlpatterns = [
    path('initial/', render_initial_data, name="product-initial"),
    path('create/', product_create_view, name="product-create"),
    path('<int:id>/', product_detail_view, name="product-detail"),
    path('<int:id>/delete', product_delete_view, name="product-delete"),
    # path('<int:id>/', dynamic_lookup_view, name="product-detail"),
    path('', product_list_view, name='product-list')
]
