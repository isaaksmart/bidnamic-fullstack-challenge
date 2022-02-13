from datetime import date
from django.forms import ModelForm
from .models import Bidnamic

from django import forms
from django.forms import ModelForm


class DateInput(forms.DateInput):
    input_type = 'date'

class BidnamicForm(ModelForm):
    
    def clean_birthday(self):
        dob = self.cleaned_data['DateOfBirth']
        age = (date.today() - dob).days / 365
        if age < 18:
            raise forms.ValidationError('You must be at least 18 years old')
        return dob

    class Meta:
        model = Bidnamic
        fields = ['Title', 'FirstName', 'Surname', 'DateOfBirth', 'CompanyName', 'Address', 'Telephone', 'BiddingSettings', 'GoogleID']
        widgets = {
            'DateOfBirth': DateInput(),
        }
