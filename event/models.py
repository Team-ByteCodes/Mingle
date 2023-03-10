from django.db import models
from UserAccounts.models import *
# Create your models here.
class Events(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True,blank=True)
    event_name = models.CharField(max_length=200,null=True,blank=True)
    registeration_limit = models.IntegerField(null=True,blank=True)
    event_description = models.TextField(null=True,blank=True)
    location = models.CharField(max_length=200,null=True,blank=True)
    date = models.DateTimeField(null=True,blank=True)
    registeration_start_date = models.DateTimeField(null=True,blank=True)
    registeration_end_date = models.DateTimeField(null=True,blank=True)
    cover_image = models.CharField(max_length=256, blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now_add=False,null=True,blank=True)

class Rate(models.Model):
    stars = models.IntegerField(null=True,blank=True)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True,blank=True)
    description = models.CharField(max_length=200,null=True,blank=True)
    event = models.ForeignKey(Events,on_delete=models.CASCADE,null=True,blank=True)

class OrganizationDetail(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True,blank=True)
    organization_address = models.TextField(null=True,blank=True)
    organization_logo = models.CharField(max_length=256, blank=True, null=True)
    social_link = models.URLField(max_length=1024, blank=True, null=True)


class Icebreakers(models.Model):
    value = models.CharField(max_length=200,null=True,blank=True)
    created_at = models.DateTimeField(auto_now=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now_add=False,null=True,blank=True)



class UserAppliedforEvents(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True,blank=True)
    event = models.ForeignKey(Events,on_delete=models.CASCADE,null=True,blank=True)
    applied_at = models.DateTimeField(auto_now=True,null=True,blank=True)

class Interest(models.Model):
    value = models.CharField(max_length=100,null=True,blank=True)
    

class Match(models.Model):
    user_1_id = models.IntegerField(null=True,blank=True)
    user_2_id = models.IntegerField(null=True,blank=True)
    approved = models.CharField(max_length=10, default='0')
    

class Interest(models.Model):
    value = models.CharField(max_length=100,null=True,blank=True)
class Passions(models.Model):
    value = models.CharField(max_length=100,null=True,blank=True)
