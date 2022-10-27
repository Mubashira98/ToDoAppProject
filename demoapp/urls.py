from django.urls import path

from demoapp import views

urlpatterns = [
    path('',views.mainpage,name='mainpage'),
    path('secondpage',views.secondpage,name='secondpage')



    ]