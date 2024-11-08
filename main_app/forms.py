from django import forms
from django.contrib.auth.forms import UserCreationForm

from main_app.models import Login, Doner, Receiver, Receiver_request, feedback


class LoginRegister(UserCreationForm):
     username= forms.CharField()
     password = forms.CharField(label="passord",widget=forms.PasswordInput)

     class Meta:
           model = Login
           fields =('username','password')
class  DonerRegister(forms.ModelForm):
    class Meta:
        model= Doner
        fields ="__all__"
        exclude =("user",)

class  ReceiverRegister(forms.ModelForm):
    class Meta:
        model= Receiver
        fields ="__all__"
        exclude =("user",)

class DateInput(forms.DateInput):
    input_type = 'date'



class  R_request(forms.ModelForm):
    date=forms.DateField(widget=DateInput)
    class Meta:
        model= Receiver_request
        fields ="__all__"
        exclude = ("ReceiverName","Status","DonerName",)

class Fdbk(forms.ModelForm):
    class Meta:
        model = feedback
        fields ="__all__"
        exclude = ("date","replay","name",)

