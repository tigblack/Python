from django.urls import path

from . import views


urlpatterns = [
    path("", views.SharkView.as_view()),
    path("<int:pk>/", views.SharkDetailView.as_view(), name="shark"),
]