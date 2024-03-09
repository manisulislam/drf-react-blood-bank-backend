from django.urls import path
from .views import UserRegisterView,VerifyUserEmail,LoginUserView,TestAuthenticationView

urlpatterns=[
    path('register/',UserRegisterView.as_view(),name='register'),
    path('verify_email/',VerifyUserEmail.as_view(),name='verify_email'),
    path('login/',LoginUserView.as_view(),name='login'),
    path('test/',TestAuthenticationView.as_view(), name='test')
]