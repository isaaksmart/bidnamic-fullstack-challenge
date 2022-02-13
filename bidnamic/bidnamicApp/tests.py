from http import HTTPStatus
from django.forms import ValidationError
from django.test import TestCase

from .forms import BidnamicForm
from .models import Bidnamic

class BidnamicTestCase(TestCase):
    def setUp(self):
        Bidnamic.objects.create(
            Title="MR", 
            FirstName="isaak",
            Surname="smart",
            DateOfBirth="1992-10-23",
            CompanyName="bidnamic",
            Address="address",
            Telephone="+123456789",
            BiddingSettings="HIGH",
            GoogleID="12345",
            )

    def test_bidnamic_get_item(self):
        """Retrieving form data from database"""
        bid_object = Bidnamic.objects.get(FirstName="isaak")
        field_object = Bidnamic._meta.get_field('FirstName')
        field_value = field_object.value_from_object(bid_object)
        self.assertEqual(field_value, 'isaak')

    def test_bidnamic_invalid_bidding_settings(self):
        form = BidnamicForm(data={
            "Title": "MR", 
            "FirstName":"isaak",
            "Surname":"smart",
            "DateOfBirth":"1992-10-23",
            "CompanyName":"bidnamic",
            "Address":"address",
            "Telephone":"+123456789",
            "BiddingSettings":"INVALID",
            "GoogleID":"12345"})

        self.assertEqual(
            form.errors["BiddingSettings"], ["Select a valid choice. INVALID is not one of the available choices."]
        )

    def test_bidnamic_invalid_dob(self):
        try:
            response = self.client.post("/", data={
                "Title": "MR", 
                "FirstName":"isaak",
                "Surname":"smart",
                "DateOfBirth":"2010-10-23",
                "CompanyName":"bidnamic",
                "Address":"address",
                "Telephone":"+123456789",
                "BiddingSettings":"HIGH",
                "GoogleID":"12345"})
        except ValidationError as e:
            self.assertEqual(str(e), "['You must be at least 18 years old']")

    def test_bidnamic_invalid_telephone(self):
        form = BidnamicForm(data={
            "Title": "Mr.", 
            "FirstName":"isaak",
            "Surname":"smart",
            "DateOfBirth":"2010-10-23",
            "CompanyName":"bidnamic",
            "Address":"address",
            "Telephone":"INVALID",
            "BiddingSettings":"HIGH",
            "GoogleID":"12345"})

        self.assertEqual(form.errors["Telephone"], ["Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."])