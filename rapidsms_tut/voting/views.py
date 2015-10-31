from django.shortcuts import render

# Create your views here.
from rapidsms.backends.http.views import GenericHttpBackendView

class MyBackendView(GenericHttpBackendView):
    params = {
        'identity_name': 'phone',
        'text_name': 'message',
    }