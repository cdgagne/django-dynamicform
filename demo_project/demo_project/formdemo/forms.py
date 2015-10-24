from django import forms
from django.core.validators import EmailValidator
from dynamicform.widgets import AjaxValidatingTextInput


class MyDynamicForm(forms.Form):
    email = forms.CharField(widget=AjaxValidatingTextInput, validators=[EmailValidator(),])
    name = forms.CharField(widget=AjaxValidatingTextInput)
