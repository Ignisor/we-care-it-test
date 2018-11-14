from django.urls import path

from accounts import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('users/list/', views.UserStatisticListView.as_view(), name='users_statistics_list'),
]
