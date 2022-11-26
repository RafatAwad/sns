from django.urls import path
from .views import profile, update_profile, admin_login, admin_logout, settings_page

urlpatterns = [
    path('login', admin_login, name='login'),
    path('logout', admin_logout, name='logout'),
    path('profile/<user_id>', profile, name='profile'),
    path('update/<user_id>', update_profile, name='update-profile'),
    path('settings/', settings_page, name='settings-page'),
]