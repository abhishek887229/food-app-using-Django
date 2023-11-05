
from django.urls import path
from . import views

#this is a namespace for our url and identification
app_name="food"

urlpatterns = [
    path("",views.base,name="base_page"),
    path("index/",views.index,name="index_page"),
    path("<int:item_id>/<str:item_name>",views.detail,name="detail_page"),
    path('add/',views.create_item,name="create_item"),
    path('update/<int:id>/',views.update_item,name="update_item"),
    path('delete/<int:id>/',views.delete_item,name="delete_item"),   
]