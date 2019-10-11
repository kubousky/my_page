from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about-us"),
    path('contact/', views.contact, name="contact"),
    path('categories/', views.categories, name='categories'),


    path('projects', views.project_list, name='project_list'),

    path('<slug:category_slug>/', views.project_list, name='project_list_by_category'),
    path('<int:id>/<slug:slug>/', views.project_detail, name='project_detail'),
]
