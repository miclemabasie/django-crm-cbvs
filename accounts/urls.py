from django.urls import path
from django.contrib.auth.views import (
    LoginView, 
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetCompleteView
)
from .views import UserCreateView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
    path('signup/', UserCreateView.as_view(), name='signup'),
    path('login', LoginView.as_view(), name='login'),
    path('login', LoginView.as_view(), name='login'),
    path('login', LoginView.as_view(), name='login'),
]