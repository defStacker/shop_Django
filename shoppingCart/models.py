# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    username = models.CharField(max_length=150)
    email = models.EmailField()
    number = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    dateInserted = models.DateTimeField(blank=True)
    contractStarted = models.DateTimeField(blank=True)
    country = models.CharField(max_length=150)
    nationalId = models.CharField(max_length=150)
    typeAccess = models.CharField(max_length=150)

class Products(models.Model):
    productName = models.CharField(max_length=150)
    serialNUmber = models.CharField(max_length=150)
    category = models.CharField(max_length=150)


class Quantity(models.Model):
    productId = Products()
    quantity = models.CharField(max_length=150)



class Clients(models.Model):
    name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    username = models.CharField(max_length=150)
    email = models.EmailField()
    number = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    date = models.DateTimeField(blank=True)
    contractStarted = models.DateTimeField(blank=True)
    country = models.CharField(max_length=150)
    nationalId = models.CharField(max_length=150)

class Sales(models.Model):
    clients = Clients()
    salesDetails = models.CharField(max_length=150)
    date = models.DateTimeField(blank=True)
    total = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    nationalId = models.CharField(max_length=150)

class History(models.Model):
    clients = models.CharField(max_length=150)
    event = models.CharField(max_length=150)
    date = models.DateTimeField(blank=True)
