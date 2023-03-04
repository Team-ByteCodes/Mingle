from django.urls import path
from UserAccounts.views import *



urlpatterns = [
    path('register', Register, name="register"),
    path('verify', VerifyOTP, name="verify-otp"),
    path('login', Login, name="login"),
]
