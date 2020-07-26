from django.db import models
from django.conf import settings
from rest_framework.authtoken.models import Token
import datetime
from django.utils.timezone import now,localtime
from django.core.validators import FileExtensionValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class SellerProfile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=False)
	phone_number=models.CharField(max_length=20,null=True,blank=True)
	image=models.FileField(null=True,blank=True,validators=[FileExtensionValidator(allowed_extensions=['jpg','jpeg','png'])])
	is_phone_number_verified=models.BooleanField(default=False,null=True,blank=False)
	is_email_verified=models.BooleanField(default=False,null=True,blank=False)
	is_seller_verified=models.BooleanField(default=True,null=True,blank=False)
	account_created_date = models.DateTimeField(default=datetime.datetime.now().replace(tzinfo=None),auto_now=False, auto_now_add=False,null=True,blank=False)
	def __str__(self):
		return self.user.username

class CustomerProfile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=False)
	phone_number=models.CharField(max_length=20,null=True,blank=True)
	image=models.FileField(null=True,blank=True,validators=[FileExtensionValidator(allowed_extensions=['jpg','jpeg','png'])])
	is_phone_number_verified=models.BooleanField(default=False,null=True,blank=False)
	is_email_verified=models.BooleanField(default=False,null=True,blank=False)
	is_customer_verified=models.BooleanField(default=True,null=True,blank=False)
	account_created_date = models.DateTimeField(default=datetime.datetime.now().replace(tzinfo=None),auto_now=False, auto_now_add=False,null=True,blank=False)
	def __str__(self):
		return self.user.username

@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None,created=False,**kwargs):
	if created:
		Token.objects.create(user=instance)