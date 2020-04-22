from django.urls import path
from property.api.views import (
    api_detail_view,
    api_update_property_view,
    #api_delete_property_view,
    #api_create_property_view,
    ApiPropertyListView,
    followview
)

app_name = 'property'

urlpatterns = [

    #path('create', api_create_property_view, name='create'),

    path('list', ApiPropertyListView.as_view(), name='list'),
    path('list1/',followview.as_view(),name='list1'),
    path('<slug>/', api_detail_view, name='detail'),
    path('<slug>/update', api_update_property_view, name='update'),
    #path('<slug>/delete', api_delete_property_view, name='delete'),


]
