from . import views
from django.urls import path

urlpatterns = [
    path('todo_week/monday', views.monday, name='leo'),
    path('todo_week/tuesday', views.tuesday, name='tuesday'),
]
