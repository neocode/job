__author__ = 'alex'

from django.contrib import admin

from dynamic_model.models import supermodel_list
for model in supermodel_list:
    admin.site.register(model)