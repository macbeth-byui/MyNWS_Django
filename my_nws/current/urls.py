from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('config', views.config, name="config"),
    path('save_config', views.save_config, name="save_config")
]