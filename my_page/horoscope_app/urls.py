from . import views
from django.urls import path

urlpatterns = [
    path('leo/', views.leo, name='leo'),
    path('scorpion/', views.scorpio, name='scorpion'),
    path('aries/', views.aries, name='aries'),
    path('taurus/', views.taurus, name='taurus'),
    path('gemini/', views.gemini, name='gemini'),
    path('cancer/', views.cancer, name='cancer'),
    path('virgo/', views.virgo, name='virgo'),
    path('libra/', views.libra, name='libra'),
    path('sagittarius/', views.sagittarius, name='sagittarius'),
    path('capricorn/', views.capricorn, name='capricorn'),
    path('aquarius/', views.sagittarius, name='aquarius'),
    path('pisces/', views.pisces, name='pisces'),
]
