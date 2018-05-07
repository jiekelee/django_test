from django.contrib import admin
from django.urls import path
# import blog.views as bv
from . import views


urlpatterns = [
    path('',views.index, name='index'),
    path('test.html',views.test),
]
