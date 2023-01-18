from django.urls import path

from . import views

urlpatterns = [
    path("doramas/", views.DoramaView.as_view()),
    path("create-dorama/", views.CreateDoramaView.as_view()),
    path("doramas/<int:pk>/", views.DoramaDetailView.as_view()),
    path("get-dorama/<int:pk>/", views.GetDoramaView.as_view()),
]