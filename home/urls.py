from django.urls import path, include
from . import views

app_name = 'home'
urlpatterns = [
    # /home/
    path('', views.index, name='indexempty'),

    # /home/<page_number>/
    path('<int:page_number>/', views.index, name='index'),

]
