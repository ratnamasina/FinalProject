from django.db import models

from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse


class user(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email_id = models.CharField(max_length=200)
    password = models.CharField(max_length=200)


class phone_brand(models.Model):
    phone_brand_id = models.IntegerField(primary_key=True)
    phone_brand_name = models.CharField(max_length=200)


class phone_modell(models.Model):
    phone_model_id = models.IntegerField(primary_key=True)
    phone_model_name = models.CharField(max_length=200)
    phone_Img = models.ImageField(upload_to='phoneimages', default="static/images/phone.png")
    phone_brand_id = models.ForeignKey(phone_brand, default=1, on_delete=models.SET_DEFAULT)


class phone_feature(models.Model):
    phone_feature_id = models.IntegerField(primary_key=True)
    phone_feature_name = models.CharField(max_length=200)
    phone_brand_id = models.ForeignKey(phone_brand, default=1, on_delete=models.SET_DEFAULT)


class phone_feature_v(models.Model):
    phone_feature_v_id = models.IntegerField(primary_key=True)
    phone_feature_id = models.ForeignKey(phone_feature, default=1, on_delete=models.SET_DEFAULT)
    phone_brand_id = models.ForeignKey(phone_brand, default=1, on_delete=models.SET_DEFAULT)
    phone_model_id = models.ForeignKey(phone_modell, default=1, on_delete=models.SET_DEFAULT)
    phone_feature_v_value = models.CharField(max_length=200)


class tab_brand(models.Model):
    tab_brand_id = models.IntegerField(primary_key=True)
    tab_brand_name = models.CharField(max_length=200)


class tab_modell(models.Model):
    tab_model_id = models.IntegerField(primary_key=True)
    tab_model_name = models.CharField(max_length=200)
    tab_Img = models.ImageField(upload_to='phoneimages', default="static/images/phone.png")
    tab_brand_id = models.ForeignKey(tab_brand, default=1, on_delete=models.SET_DEFAULT)


class tab_feature(models.Model):
    tab_feature_id = models.IntegerField(primary_key=True)
    tab_feature_name = models.CharField(max_length=200)
    tab_brand_id = models.ForeignKey(tab_brand, default=1, on_delete=models.SET_DEFAULT)


class tab_feature_v(models.Model):
    tab_feature_v_id = models.IntegerField(primary_key=True)
    tab_feature_id = models.ForeignKey(tab_feature, default=1, on_delete=models.SET_DEFAULT)
    tab_brand_id = models.ForeignKey(tab_brand, default=1, on_delete=models.SET_DEFAULT)
    tab_model_id = models.ForeignKey(tab_modell, default=1, on_delete=models.SET_DEFAULT)
    tab_feature_v_value = models.CharField(max_length=200)


class watch_brand(models.Model):
    watch_brand_id = models.IntegerField(primary_key=True)
    watch_brand_name = models.CharField(max_length=200)


class watch_modell(models.Model):
    watch_model_id = models.IntegerField(primary_key=True)
    watch_model_name = models.CharField(max_length=200)
    watch_Img = models.ImageField(upload_to='phoneimages', default="static/images/phone.png")
    watch_brand_id = models.ForeignKey(watch_brand, default=1, on_delete=models.SET_DEFAULT)


class watch_feature(models.Model):
    watch_feature_id = models.IntegerField(primary_key=True)
    watch_feature_name = models.CharField(max_length=200)
    watch_brand_id = models.ForeignKey(watch_brand, default=1, on_delete=models.SET_DEFAULT)


class watch_feature_v(models.Model):
    watch_feature_v_id = models.IntegerField(primary_key=True)
    watch_feature_id = models.ForeignKey(watch_feature, default=1, on_delete=models.SET_DEFAULT)
    watch_brand_id = models.ForeignKey(watch_brand, default=1, on_delete=models.SET_DEFAULT)
    watch_model_id = models.ForeignKey(watch_modell, default=1, on_delete=models.SET_DEFAULT)
    watch_feature_v_value = models.CharField(max_length=200)

