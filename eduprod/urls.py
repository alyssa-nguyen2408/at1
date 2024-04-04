from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views


app_name = 'eduprod'

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('chemistry/', views.chemistry, name='chemistry'),  # URL for chemistry page
    path('english/', views.english, name='english'),  # URL for english page
    path('tests/', views.tests, name='tests'),  # URL for tests page
    path('engmod1/', views.engmod1, name='engmod1'),  # URL for engmod1 page
    path('submit_essay/', views.submit_essay, name='submit_essay'),#URL for submit essay page
    path('essay_list/', views.essay_list, name='essay_list'),#URL for essay list page
]
