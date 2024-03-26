from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

#from django.urls import path
#from . import views

#urlpatterns = [
    # Other URL patterns
    #path('folder1/', views.folder1_view, name='folder1_view'),
    #path('', views.index, name='index'),
#]