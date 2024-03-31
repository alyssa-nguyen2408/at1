from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

#urlpatterns = [
#    path('', login_required(views.index), name='index'),
#    path('index/', login_required(views.index), name='index'),  # Ensure both URLs are protected
#]

urlpatterns = [
    #path('', views.home, name='home'),
    #path('index/', views.index, name='index')
    path('', views.index, name='index'),#landing page url
    path('home/', views.home, name='home'),
]

#urlpatterns = [
    # Change the path from '' to 'home/'
#    path('home/', views.home, name='home'),
    # Leave the existing index URL pattern as is
#    path('index/', views.index, name='index'),
#]