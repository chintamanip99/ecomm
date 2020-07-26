from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,renderer_classes,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.utils.timezone import now,localtime
import datetime
import random
from django.core.mail import send_mail,BadHeaderError
from rest_framework.permissions import BasePermission
from datetime import timedelta
from .serializers import SellerProfile,CustomerProfile
from .serializers import SellerProfileSerializer,CustomerProfileSerializer
from rest_framework.authtoken.views import ObtainAuthToken

# Create your views here.

class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        is_seller=False
        is_customer=False
        try:
        	SellerProfile.objects.get(user=token.user)
        	is_seller=True
        except SellerProfile.DoesNotExist:
        	is_seller=False
        try:
        	CustomerProfile.objects.get(user=token.user)
        	is_customer=True
        except CustomerProfile.DoesNotExist:
        	is_customer=False
        return Response({'token': token.key, 'username': token.user.username,'is_seller':is_seller,'is_customer':is_customer})

@api_view(['POST'])
@permission_classes([])
def register_seller(request):

    if request.method=='POST':
        serializer=SellerProfileSerializer(data=request.data)
        data={}
        if(serializer.is_valid()):
            profile=serializer.save()
            data['username']=profile.user.username
            data['first_name']=profile.user.first_name
            data['last_name']=profile.user.last_name
            data['email']=profile.user.email
            data['password']=profile.user.password
            token=Token.objects.get(user=profile.user).key
            data['token']=token
        else:
            data=serializer.errors
        return Response(data)

@api_view(['POST'])
@permission_classes([])
def register_customer(request):

    if request.method=='POST':
        serializer=CustomerProfileSerializer(data=request.data)
        data={}
        if(serializer.is_valid()):
            profile=serializer.save()
            data['username']=profile.user.username
            data['first_name']=profile.user.first_name
            data['last_name']=profile.user.last_name
            data['email']=profile.user.email
            data['password']=profile.user.password
            token=Token.objects.get(user=profile.user).key
            data['token']=token
        else:
            data=serializer.errors
        return Response(data)
