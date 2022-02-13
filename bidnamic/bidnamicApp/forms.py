from django.forms import DateField, ModelForm
from .models import Bidnamic

from django import forms
from django.forms import ModelForm


class DateInput(forms.DateInput):
    input_type = 'date'

class BidnamicForm(ModelForm):
    # DateOfBirth = DateField(input_formats='%d/%m/%YYYY', label="Date of Birth")
    class Meta:
        model = Bidnamic
        fields = ['Title', 'FirstName', 'Surname', 'DateOfBirth', 'CompanyName', 'Address', 'Telephone', 'BiddingSettings', 'GoogleID']
        widgets = {
            'DateOfBirth': DateInput(),
        }
