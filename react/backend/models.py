from django.db import models
from datetime import date
# Create your models here.

class Info(models.Model):
    COUNTRY_CHOICES = [
        ("NG", "Nigeria" ),
        ( "GH", "Ghana"),
        ( "MB","Mozambique"),
        ( "SA","South Africa"),
        ("NI", "Niger"),
        ("TG", "Togo" ),
        ("ZA", "Zambia" ),
        ("BN", "Benin Republic" ),
        ("CM", "Cameroun" ), 
        ("BT", "Botswana" ),
        ( "MA", "Mali" ),
        ("ZI" ,"Zimbabwe" ),
        ( "AN", "Angola" )
    ]
    country_name= models.CharField(max_length = 50, choices=COUNTRY_CHOICES ,default='unknown')
    cases=models.IntegerField(default=1)
    test_completed = models.IntegerField(default=1)
    deaths = models.IntegerField(default=1)
    date_update = models.DateField(default=date.today)
    vaccine_total_doses = models.IntegerField(default=1)