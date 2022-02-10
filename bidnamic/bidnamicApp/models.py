from django.db import models
from django.core.validators import RegexValidator

TITLE_CHOICES = [
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
]

BID_CHOICES = [
    ('HIGH', 'HIGH'),
    ('MEDIUM', 'MEDIUM'),
    ('LOW', 'LOW'),
]


class Bidnamic(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

    Title = models.CharField(max_length=3, choices=TITLE_CHOICES)
    FirstName = models.CharField(max_length=100, verbose_name=u"First Name")
    Surname = models.CharField(max_length=100)
    DateOfBirth = models.DateField(blank=True, null=True, verbose_name=u"Date of Birth")
    CompanyName = models.CharField(max_length=100, verbose_name=u"Company Name")
    Address = models.CharField(max_length=100)
    Telephone = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    BiddingSettings = models.CharField(max_length=100, verbose_name=u"Bidding Settings", choices=BID_CHOICES)
    GoogleID = models.CharField(max_length=100, verbose_name=u"Google Ads Account ID")