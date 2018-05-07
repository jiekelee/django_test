from django.urls import path
# from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index),
    path('result.html',views.result_cloud),
    path('list.html',views.listall),
    path('delete/(?P<file_id>.+)$',views.delete_view,name='delete'),
]