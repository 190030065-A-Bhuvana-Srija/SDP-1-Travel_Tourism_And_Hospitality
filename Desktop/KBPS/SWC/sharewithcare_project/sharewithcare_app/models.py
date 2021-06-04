from cart.cart import Cart
from django.db import models
from django.db.models import Model
from django.db.models.signals import post_save

from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

class Add(models.Model):
    rawname = models.CharField(max_length=40)
    quantity = models.IntegerField(
        blank=False,
        default=1,
        help_text=("Amount in stock")
    )
    image = models.ImageField(upload_to='rawproducts/', blank=True)


class List(models.Model):
    categoryname = models.CharField(max_length=40)
    numberofvarieties = models.IntegerField()
    collage = models.ImageField(upload_to='listofinterproducts/', blank=True)


class Add2(models.Model):
    intername = models.CharField(max_length=40)
    quantity = models.IntegerField(
        blank=False,
        default=1,
        help_text=("Amount in stock")
    )
    image = models.ImageField(upload_to='interproducts/', blank=True)


class Add3(models.Model):
    endname = models.CharField(max_length=40)
    brandname = models.CharField(max_length=40)
    price = models.IntegerField()
    quantity = models.IntegerField(
        blank=False,
        default=1,
        help_text=("Amount in stock")
    )
    image = models.ImageField(upload_to='endproducts/', blank=True)


class pay(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    amount = models.IntegerField()

class SweetsModel(models.Model):
    name = models.CharField(max_length=40)
    quantity = models.IntegerField(
        blank=False,
        default=1,
        help_text=("Amount in stock")
    )
    price = models.IntegerField()
    image = models.ImageField(upload_to='sweets/', blank=True)

class BeveragesModel(models.Model):
    name = models.CharField(max_length=40)
    quantity = models.IntegerField(
        blank=False,
        default=1,
        help_text=("Amount in stock")
    )
    price = models.IntegerField()
    image = models.ImageField(upload_to='beverages/', blank=True)

class CakesModel(models.Model):
    name = models.CharField(max_length=40)
    quantity = models.IntegerField(
        blank=False,
        default=1,
        help_text=("Amount in stock")
    )
    price = models.IntegerField()
    image = models.ImageField(upload_to='cakes/', blank=True)

class KulfisModel(models.Model):
    name = models.CharField(max_length=40)
    quantity = models.IntegerField(
        blank=False,
        default=1,
        help_text=("Amount in stock")
    )
    price = models.IntegerField()
    image = models.ImageField(upload_to='kulfis/', blank=True)

class DairyModel(models.Model):
    name = models.CharField(max_length=40)
    quantity = models.IntegerField(
        blank=False,
        default=1,
        help_text=("Amount in stock")
    )
    price = models.IntegerField()
    image = models.ImageField(upload_to='dairy/', blank=True)

class CurdModel(models.Model):
    name = models.CharField(max_length=40)
    quantity = models.IntegerField()
    brand = models.CharField(max_length=40)
    price = models.IntegerField()
    image = models.ImageField(upload_to='curd/', blank=True)

class GheeModel(models.Model):
    name = models.CharField(max_length=40)
    quantity = models.IntegerField()
    brand = models.CharField(max_length=40)
    price = models.IntegerField()
    image = models.ImageField(upload_to='ghee/', blank=True)

class ButterModel(models.Model):
    name = models.CharField(max_length=40)
    quantity = models.IntegerField()
    brand = models.CharField(max_length=40)
    price = models.IntegerField()
    image = models.ImageField(upload_to='butter/', blank=True)

class PaneerModel(models.Model):
    name = models.CharField(max_length=40)
    quantity = models.IntegerField()
    brand = models.CharField(max_length=40)
    price = models.IntegerField()
    image = models.ImageField(upload_to='paneer/', blank=True)

class CreamModel(models.Model):
    name = models.CharField(max_length=40)
    quantity = models.IntegerField()
    brand = models.CharField(max_length=40)
    price = models.IntegerField()
    image = models.ImageField(upload_to='cream/', blank=True)

class BestSellers(models.Model):
    name = models.CharField(max_length=40)
    quantity = models.IntegerField(
        blank=False,
        default=1,
        help_text=("Amount in stock")
    )
    brand = models.CharField(max_length=40)
    price = models.IntegerField()
    image = models.ImageField(upload_to='bestsellers/', blank=True)





