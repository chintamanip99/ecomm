from rest_framework import serializers
from django.contrib.auth.models import User
import datetime
import random
import re
from django.core.mail import send_mail,BadHeaderError
from .models import SellerProfile,CustomerProfile

class CustomerProfileSerializer(serializers.ModelSerializer):
	password2=serializers.CharField(write_only=True,required=True)
	email=serializers.CharField(write_only=True,required=False)
	phone_number=serializers.CharField(write_only=True,required=True)
	first_name=serializers.CharField(write_only=True,required=False)
	last_name=serializers.CharField(write_only=True,required=False)
	image=serializers.FileField(write_only=True,required=False)
	class Meta:
		model=User
		fields=['username','email','password','password2','image','first_name','last_name','phone_number']

	def save(self):
		username=self.validated_data['username']
		password=self.validated_data['password']
		password2=self.validated_data['password2']
		phone_number=self.validated_data['phone_number']
		if(len(phone_number)<10):
			raise serializers.ValidationError({'phone_number':'Phone Number entered is invalid'})
		if('image' in self.validated_data.keys()):
			image=self.validated_data['image']
		if('email' in self.validated_data.keys()):
			email=self.validated_data['email']
			regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
			if not re.search(regex,email):
				raise serializers.ValidationError({'email':'Email entered is invalid'})
		if password!=password2:
			raise serializers.ValidationError({'password':'Passwords doesnt match'})			
		else:
			user=User.objects.create_user(
				username=username,
				password=password
			)
			if('first_name' in self.validated_data.keys()):
				user.first_name=self.validated_data['first_name']
			if('last_name' in self.validated_data.keys()):
				user.last_name=self.validated_data['last_name']
			if('email' in self.validated_data.keys()):
				user.email=self.validated_data['email']
			user.save()
			profile=CustomerProfile.objects.create(
				user=user,
				phone_number=phone_number,
			)
			if('image' in self.validated_data.keys()):
				profile.image=image
			profile.save()
			return profile

class SellerProfileSerializer(serializers.ModelSerializer):
	password2=serializers.CharField(write_only=True,required=True)
	email=serializers.CharField(write_only=True,required=False)
	phone_number=serializers.CharField(write_only=True,required=True)
	first_name=serializers.CharField(write_only=True,required=False)
	last_name=serializers.CharField(write_only=True,required=False)
	image=serializers.FileField(write_only=True,required=False)
	class Meta:
		model=User
		fields=['username','email','password','password2','image','first_name','last_name','phone_number']

	def save(self):
		username=self.validated_data['username']
		password=self.validated_data['password']
		password2=self.validated_data['password2']
		phone_number=self.validated_data['phone_number']
		if(len(phone_number)<10):
			raise serializers.ValidationError({'phone_number':'Phone Number entered is invalid'})
		if('image' in self.validated_data.keys()):
			image=self.validated_data['image']
		if('email' in self.validated_data.keys()):
			email=self.validated_data['email']
			regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
			if not re.search(regex,email):
				raise serializers.ValidationError({'email':'Email entered is invalid'})
		if password!=password2:
			raise serializers.ValidationError({'password':'Passwords doesnt match'})			
		else:
			user=User.objects.create_user(
				username=username,
				password=password
			)
			if('first_name' in self.validated_data.keys()):
				user.first_name=self.validated_data['first_name']
			if('last_name' in self.validated_data.keys()):
				user.last_name=self.validated_data['last_name']
			if('email' in self.validated_data.keys()):
				user.email=self.validated_data['email']
			user.save()
			profile=SellerProfile.objects.create(
				user=user,
				phone_number=phone_number,
			)
			if('image' in self.validated_data.keys()):
				profile.image=image
			profile.save()
			return profile