from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView,LogoutView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns=[
    path('', views.index, name='index'),
    path('register/', views.reg, name='register'),
    path('login/', LoginView.as_view(template_name='acc/login.html'), name='login'),

    path('logout/', LogoutView.as_view(template_name='acc/logout.html'),name='logout'),

    path('profile/', views.profile, name='profile'),

    path('profile/edit', views.edit_profile, name='edit_profile'),

    path('edit_password/', views.edit_pass, name='edit_pass'),

    path('password/', PasswordResetView.as_view(template_name='acc/pass_reset.html'),name='pass_reset'),

    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', PasswordResetConfirmView.as_view(),
        {'template_name': 'accounts/reset_password_confirm.html',
         'post_reset_redirect': 'accounts:password_reset_complete'}, name='password_reset_confirm'),

    path('password-reset/done/',PasswordResetDoneView.as_view(template_name='acc/password_reset_done.html'),
         name='password_reset_done'),

    path('password-reset-complete/', PasswordResetCompleteView.as_view(template_name='acc/password_reset_complete.html'),
         name='password_reset_complete'),
]