from django.urls import path
from django.contrib.auth.views import LogoutView
from .import views

urlpatterns = [
    path('register/',views.register,name='register'),
    # path('login/',views.user_login,name='login'),
    path('login/',views.UserLogin.as_view(),name='login'),

    path('profile/',views.profile,name='profile'),
    path('pass_change/',views.pass_change,name='pass_change'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
    # path('LogOut/',views.LogOut,name='LogOut'),
    # path('LogOut/',LogoutView.as_view(),name='LogOut'),
    path('LogOut/',views.CustomLogoutView.as_view(),name='LogOut'),
]
