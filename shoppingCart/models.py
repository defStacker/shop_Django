# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from mongoengine import Document, EmbeddedDocument, fields


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


class Author(Document):
    name = fields.StringField()


class Book(Document):
    name = fields.StringField()
    author = fields.ReferenceField(Author, dbref=True)


class ToolInput(EmbeddedDocument):
    id = fields.StringField(required=True)
    type = fields.ListField(fields.DynamicField(null=True))
    label = fields.StringField(required=True, null=True)
    description = fields.StringField(required=False, null=True)
    default = fields.DynamicField(required=False)
    inputBinding = fields.DynamicField(required=True)
    required = fields.BooleanField(required=False, default=True)


class ToolOutput(EmbeddedDocument):
    id = fields.StringField(required=True)
    type = fields.ListField(fields.DynamicField(null=True))
    label = fields.StringField(required=False)
    default = fields.DynamicField(required=False, null=True)
    description = fields.StringField(required=False)
    outputBinding = fields.DynamicField(required=False)
    required = fields.BooleanField(required=False, default=True)


class Tool(Document):
    id = fields.StringField(required=True, primary_key=True)
    # 'class' is a reserved word in python, so to get a field called "class", we use the following trick with vars():
    vars()['class'] = fields.StringField(verbose_name="class", required=True)
    label = fields.StringField(required=True)
    description = fields.StringField(required=True, null=True)
    owner = fields.ListField(fields.StringField())
    contributor = fields.ListField(fields.StringField())
    inputs = fields.EmbeddedDocumentListField(ToolInput)
    outputs = fields.EmbeddedDocumentListField(ToolOutput)
    baseCommand = fields.DynamicField(required=True)
    arguments = fields.DynamicField(required=True)
    requirements = fields.DynamicField(required=True, null=True)
    hints = fields.DynamicField(required=False, null=True)
    cwlVersion = fields.StringField(required=False, null=True, choices=['cwl:draft-2'])
    stdin = fields.StringField(required=False, null=True)
    stdout = fields.StringField(required=False, null=True)
    successCodes = fields.ListField(fields.IntField(), required=False)
    temporaryFailCodes = fields.ListField(fields.IntField(), required=False)
    permanentFailCodes = fields.ListField(fields.IntField(), required=False)
