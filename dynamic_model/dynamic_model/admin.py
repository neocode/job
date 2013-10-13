__author__ = 'alex'

from django.contrib import admin

from dynamic_model.models import model_list
'''
for model in supermodel_list:
    admin.site.register(model)
'''
for model in model_list:
    admin.site.register(model)