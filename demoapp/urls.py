from django.urls import path

from demoapp import views

urlpatterns = [
    path('',views.mainpage,name='mainpage'),
    path('add_todo',views.add_todo,name='add_todo'),
    path('viewtitle',views.viewtitle,name='viewtitle'),
    path('mainpage',views.mainpage,name='mainpage'),




    ]