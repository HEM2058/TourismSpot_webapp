from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
   path('',views.Index,name="index"),
   path('RegisterForm',views.RegisterForm,name="registerform"),
   path('Register',views.Register,name="register"),
   path('otppage',views.OtpPage,name="otppage"),
   path('OtpConfirm',views.OtpConfirm,name="otpconfirm"),
   path('Loginuser',views.Loginuser,name="loginuser"),
   path('loginpage',views.LoginPage,name="loginpage"),
   path('updateprofile<int:pk>',views.UpdateProfile,name="updateprofile"),
   path('profile',views.Profile,name="profile"),
   path('post',views.Post,name="post"),
   path('CompanyLogout',views.CompanyLogout,name="companylogout")

   
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)