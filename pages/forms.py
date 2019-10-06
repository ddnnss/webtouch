from django.forms import ModelForm

from .models import *


class CallbackForm(ModelForm):
    class Meta:
        model = Callback
        fields = (
            'name',
            'company',
            'phone',
            'email',
            'message',
        )
