from django.urls import path

from rest_framework_simplejwt import views as jwt_views 

from account import views 

urlpatterns = [
    path('reqister/', views.RegisterUserView.as_view())
]