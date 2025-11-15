from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects_list, name='projects_list'),
    path('projects/<slug:slug>/', views.project_detail, name='project_detail'),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('resume/', views.resume, name='resume'),
    path('contact/', views.contact, name='contact'),

]