from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
]

#urlpatterns = [
    # Change the path from '' to 'home/'
#    path('home/', views.home, name='home'),
    # Leave the existing index URL pattern as is
#    path('index/', views.index, name='index'),
#]