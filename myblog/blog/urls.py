from django.contrib import admin
from django.urls import path
# import blog.views as bv
from . import views

app_name = 'blog'
urlpatterns = [
    path('',views.index, name='index'),
    # path('test.html',views.test),
    path(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
]

