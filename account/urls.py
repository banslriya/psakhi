from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns = [
	path('password_reset',
        auth_views.PasswordResetView.as_view(template_name='registration/passwordreset.html'), name='pasre'),
    path('password_reset_done/',
        auth_views.PasswordResetDoneView.as_view(template_name='registration/passwordresetdone.html'), name='password_reset_done'),        
    path('password_reset_confirm/<uidb64>/<token>',
        auth_views.PasswordResetConfirmView.as_view(template_name='registration/passwordresetcomplete.html'), name='password_reset_confirm'),
    path('password_reset_complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name='registration/passwordresetconfirm.html'), name='password_reset_complete'),
    path('sign-up',views.sign_up, name='sign-up'),
    path('profile',views.profile, name='profile'),
    path('profile/<int:id>/edit',views.edit_profile, name='edit_profile'),
    path('profile/medicine-donations',views.donation_list, name='donations'),
]
