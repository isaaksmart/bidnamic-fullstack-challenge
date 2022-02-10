from django.forms import ModelForm
from .models import Bidnamic

class BidnamicForm(ModelForm):
    class Meta:
        model = Bidnamic
        fields = ['Title', 'FirstName', 'Surname', 'DateOfBirth', 'CompanyName', 'Address', 'Telephone', 'BiddingSettings', 'GoogleID']
    
