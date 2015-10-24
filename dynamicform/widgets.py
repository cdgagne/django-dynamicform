from django import forms
from django.forms.utils import flatatt
from django.utils import formats
from django.utils.encoding import force_text
from django.utils.html import format_html


class AjaxValidatingTextInput(forms.TextInput):
    def __init__(self, *args, **kwargs):
        super(AjaxValidatingTextInput, self).__init__(*args, **kwargs)
        self.attrs = {'class': 'ajax-validate'}

    def render(self, name, value, attrs=None):
        if value is None:
            value = ''
        final_attrs = self.build_attrs(attrs, type=self.input_type, name=name)
        if value != '':
            # Only add the 'value' attribute if a value is non-empty.
            final_attrs['value'] = force_text(self._format_value(value))
        input_html = format_html('<input{} />', flatatt(final_attrs))
        error_div_attrs = {
                'id': 'form_error_%s' % final_attrs['id']
            }
        error_div = '<div><span class="error-container label label-danger"{}></span></div>'
        error_div_html = format_html(error_div, flatatt(error_div_attrs))
        return '%s%s' % (input_html, error_div_html)
