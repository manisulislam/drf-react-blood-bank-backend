from django.urls import path
from .views import UserRegisterView,VerifyUserEmail,LoginUserView,TestAuthenticationView,PasswordResetRequestView,PasswordResetConfirmView,SetNewPasswordView,LogOutUserView,UserInfoView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns=[
    path('register/',UserRegisterView.as_view(),name='register'),
    path('verify_email/',VerifyUserEmail.as_view(),name='verify_email'),
    path('login/',LoginUserView.as_view(),name='login'),
    path('test/',TestAuthenticationView.as_view(), name='test'),
    path('password_reset/',PasswordResetRequestView.as_view(),name='password_reset'),
    path('password_reset_confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('set_new_password/',SetNewPasswordView.as_view(), name='set_new_password'),
    path('logout/',LogOutUserView.as_view(), name='logout'),
    path("token/refresh/",TokenRefreshView.as_view(), name="token_refresh"),
    path("user_info/", UserInfoView.as_view(), name="user_info")
]