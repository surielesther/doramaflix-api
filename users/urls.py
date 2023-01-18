from django.urls import path

from . import views

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("users/", views.RegisterView.as_view()),
    path("users/<int:pk>/", views.UserDetailView.as_view()),
    path('users/login/', TokenObtainPairView.as_view()),
    path('users/refresh/', TokenRefreshView.as_view()),
]