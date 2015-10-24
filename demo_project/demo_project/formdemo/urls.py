from django.conf.urls import include, url

from formdemo.views import MyDynamicFormView

urlpatterns = [
    url(r'^/?$', MyDynamicFormView.as_view(), name='formdemo'),
]
