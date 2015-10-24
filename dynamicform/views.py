import json

from django.http import HttpResponse
from django.views.generic.base import View


class DynamicFormView(View):
    """
    Abstract class based view.
    """
    # The Django form class to validate on an Ajax GET with a validate parameter.
    form_class = None

    def get(self, request, *args, **kwargs):
        """
        Handle requests with the following format:
        http://host/url?validate=<form field name|empty>
        If the validate parameter specifies a field it will validate only that field and return
        the error. If the validate parameter is empty it will validate the entire form and return
        all errors in a list.
        """
        if request.is_ajax():
            field = request.GET.get('validate')
            form = self.form_class(request.GET)
            if not form.is_valid():
                if field and field in form.errors:
                    return HttpResponse(json.dumps({'error': form.errors[field][0]}), content_type="application/json")
                elif not field:
                    error_list = dict((key, val[0]) for key, val in form.errors.iteritems())
                    return HttpResponse(json.dumps({'errors': error_list}), content_type="application/json")
                else:
                    return HttpResponse()
            else:
                return HttpResponse(json.dumps({'data': ''}), content_type="application/json")
