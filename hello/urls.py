from django.urls import path
from django.views.generic import TemplateView
from . import views



app_name = 'hello'
urlpatterns = [
    path('', TemplateView.as_view(template_name='main')),
    path('cookie', views.cookie),
    path('hello/', views.sessfun),



]