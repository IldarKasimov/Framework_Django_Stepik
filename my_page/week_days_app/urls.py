from . import views
from django.urls import path

urlpatterns = [
    path('monday/', views.monday, name='leo'),
    path('tuesday/', views.tuesday, name='tuesday'),
]
