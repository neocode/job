__author__ = 'alex'
from django.forms import ModelForm
#from dynamic_model.forms import form_list
from django.shortcuts import render
from dynamic_model.models import model_list



def index(request):
    context = {'table1': model_list[0].objects.all(), 'table2': model_list[1].objects.all()}
    return render(request, 'index.html', context)