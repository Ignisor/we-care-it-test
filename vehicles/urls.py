from django.urls import path

from vehicles import views

urlpatterns = [
    path('list/', views.VehicleDistanceListView.as_view(), name='vehicles_list'),
]
