__author__ = 'alex'
from dynamic_model.models import model_list
from django.forms import ModelForm

def make_model_form(model):
    class _Form(ModelForm):
        class Meta:
            model = model
    return _Form

form_list = []
for model in model_list:
    form_list.append(make_model_form(model))