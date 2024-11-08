import django_filters
from django import forms
from django_filters import CharFilter

from main_app.models import Receiver_request


class BloodFilter(django_filters.FilterSet):
    Blood= CharFilter(label="",lookup_expr='icontains',widget=forms.TextInput(attrs={
        'placeholder':"search BloodGroup",'class':'form-control'
    }))
    class Meta:
        model=Receiver_request
        fields =('Blood',)