from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register
urlpatterns = [
# Authentication Views
    path('register/', register, name='web-register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='web-login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/user/login/',extra_context={'message':'You have been logged out!'}), name='web-logout'),
]
