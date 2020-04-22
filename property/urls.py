from django.urls import path
from property.views import(
    create_property_view,
    detail_property_view,
    edit_property_view,
    check_price
)

app_name = 'property'

urlpatterns = [
    path('<slug>/price', check_price, name="price"),
    path('create/', create_property_view, name="create"),
    path('<slug>/', detail_property_view, name="detail"),
    path('<slug>/edit', edit_property_view, name="edit"),
]
