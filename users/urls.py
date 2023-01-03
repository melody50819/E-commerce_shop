from django.urls import path, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView
from users.views import profile, password_change_done, register, password_reset_done, passeord_reset_complete

app_name = 'users'

urlpatterns = [
    path(
        'login/', 
        LoginView.as_view(template_name='users/login.html'), 
        name='login'),

    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path(
        'password-change/',
        PasswordChangeView.as_view(
            template_name='users/password_change.html',
            success_url=reverse_lazy('users:password_change_done'), #reverse_lazy解析路徑名稱
        ),
        name='password_change',
    ),
    path('password-change-done/', password_change_done, name='password_change_done'),
    path('register/', register, name='register'),

    path(
        'password-reset/', 
        PasswordResetView.as_view(
            template_name='users/password_reset.html',
            email_template_name='users/email/password_reset_email.html',
            subject_template_name='users/email/password_reset_subject_txt',
            success_url=reverse_lazy('users:password_reset_done'), #reverse_lazy解析路徑名稱

    ), name='password_reset'),

    path('password-reset-done/', password_reset_done, name='password_reset_done'),
    path(
        'reset/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(
            template_name='users/email/password_reset_confirm.html',
            success_url=reverse_lazy('users:reset_complete'),
        ),
        name='reset',
    ),
    path('reset-complete/', passeord_reset_complete, name='reset_complete')
]