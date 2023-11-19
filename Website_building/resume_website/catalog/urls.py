from django.urls import path
from . import views


urlpatterns = [
    path("index/",views.my_index,name="index_url"),
    path("add_data/",views.add_data,name="add_data_url"),
    path("renew_data/",views.renew_data,name="renew_data_url"),
    path('search/', views.search),
]