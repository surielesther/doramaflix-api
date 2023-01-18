from django.urls import path

from . import views

urlpatterns = [
    path("reviews/dorama/<int:pk>/", views.DoramaReviewView.as_view()),
    path("reviews/user/<int:pk>/", views.UserReviewView.as_view()),
]