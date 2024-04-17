from . import views
from django.urls import path

urlpatterns = [
    path('horoscope/leo/', views.leo, name='leo'),
    path('horoscope/scorpion/', views.scorpio, name='scorpion'),
    path('horoscope/aries/', views.aries, name='aries'),
    path('horoscope/taurus/', views.taurus, name='taurus'),
    path('horoscope/gemini/', views.gemini, name='gemini'),
    path('horoscope/cancer/', views.cancer, name='cancer'),
    path('horoscope/virgo/', views.virgo, name='virgo'),
    path('horoscope/libra/', views.libra, name='libra'),
    path('horoscope/sagittarius/', views.sagittarius, name='sagittarius'),
    path('horoscope/capricorn/', views.capricorn, name='capricorn'),
    path('horoscope/aquarius/', views.sagittarius, name='aquarius'),
    path('horoscope/pisces/', views.pisces, name='pisces'),
]
