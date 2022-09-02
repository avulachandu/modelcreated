from socket import fromshare
from django import forms
from app1.models import Raj

#create forms here
class RajForm(forms.ModelForm):
    class Meta:
        model = Raj
        fields = '__all__'

class RajForm2(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=100)
    place = forms.CharField(max_length=100)
    phonenumber = forms.IntegerField()
    course = forms.CharField(max_length=50)