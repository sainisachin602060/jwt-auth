from django.contrib import admin
from django.urls import path

from accounts.views.SignupView import SignupView
from accounts.views.LoginView import LoginView
from rest_framework_simplejwt.views import TokenRefreshView
from accounts.views.OtpRequest import OtpRequest
from accounts.views.OtpVerfiyView import OtpVerfiyView
from accounts.views.create_new_pass import Create_New_Pass
from accounts.views.ResendOtp import ResendOtp

urlpatterns = [
    path('signup/',SignupView.as_view(),name="signup"),
    path('login/',LoginView.as_view(),name="login"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('otprequest/',OtpRequest.as_view(),name="otprequest"),
    path('otpverify/',OtpVerfiyView.as_view(),name="otp verify"),
    path("newpassword/",Create_New_Pass.as_view(),name="new pass"),
    path('resendotp/',ResendOtp.as_view(),name="resendotp")
]