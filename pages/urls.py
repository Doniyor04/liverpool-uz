from django.urls import path

from pages import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('stadium/', views.stadium_page, name='stadium_page'),
    path('contact/', views.contact_page, name='contact_page'),
    path('club-history/', views.club_history_page, name='club_history'),
]