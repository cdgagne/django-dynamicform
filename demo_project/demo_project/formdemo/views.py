from django.http import HttpResponse
from django.shortcuts import render
from dynamicform.views import DynamicFormView
from formdemo.forms import MyDynamicForm

import json


class MyDynamicFormView(DynamicFormView):
    form_class = MyDynamicForm

    def get(self, request, *args, **kwargs):
        response = super(MyDynamicFormView, self).get(request, *args, **kwargs)
        if response:
            return response

        form = self.form_class(request.GET)
        context = {'form': form}
        return render(request, 'dynamicform.html', context=context)

    def post(self, request, *args, **kwargs):
        form = MyDynamicForm(request.POST)
        if form.is_valid():
            name = request.POST['name']
            email = request.POST['email']
            context = {'email': email, 'name': name}
            return render(request, 'thanks.html', context=context)
        else:
            context = {'form': form}
            return render(request, 'dynamicform.html', context)
