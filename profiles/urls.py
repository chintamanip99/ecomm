from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token
from profiles.views import register_seller,register_customer,CustomObtainAuthToken

app_name="profiles"
urlpatterns = [
    path("login_user/",CustomObtainAuthToken.as_view(),name="CustomObtainAuthToken"),
    path("register_seller/",register_seller,name="register_seller"),
    path("register_customer/",register_customer,name="register_customer"),
]