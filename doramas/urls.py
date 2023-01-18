from django.urls import path

from . import views

urlpatterns = [
    path("doramas/", views.DoramaView.as_view()),
    path("doramas/<int:pk>/", views.DoramaDetailView.as_view()),
]