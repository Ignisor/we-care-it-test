from django.urls import path

from journeys import views

urlpatterns = [
    path('create/', views.JourneyCreateView.as_view(), name='journey_create'),
]
