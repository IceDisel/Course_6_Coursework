from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from users.apps import UsersConfig
from users.views import RegisterView, ConfirmRegistrationUserView, CustomPasswordResetView, PasswordRecoveryMessageView, \
    UserListView, UserUpdateView

app_name = UsersConfig.name

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('confirm/', ConfirmRegistrationUserView.as_view(), name='confirm'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('reset/', CustomPasswordResetView.as_view(), name='reset'),
    path('reset/confirm/', PasswordRecoveryMessageView.as_view(), name='password_reset_confirm'),
    path('list_users/', UserListView.as_view(), name='list_users'),
    path('edit_users/<int:pk>', UserUpdateView.as_view(), name='edit_users'),
]