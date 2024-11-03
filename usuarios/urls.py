from django.urls import path
from django.contrib.auth.views import LoginView
from .views import RegisterView,LogoutView

urlpatterns = [
    path('register/',RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
