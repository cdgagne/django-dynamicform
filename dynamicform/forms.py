from django.forms import Form
from django.forms.utils import ErrorDict

class DynamicErrorDict(ErrorDict):
    def as_ul(self):
        # TODO Custom render here w/ error div
        raise

class DynamicForm(Form):
    @property
    def errors(self):
        return DynamicErrorDict(self, super(forms.Form, self).errors)
