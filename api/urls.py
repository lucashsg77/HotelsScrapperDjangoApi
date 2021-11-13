from django.urls import path
from api import views
urlpatterns = [
    path('', views.HotelList.as_view()),
    path('<int:pk>/', views.HotelDetail.as_view()),
    ]