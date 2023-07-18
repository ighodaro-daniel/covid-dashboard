from rest_framework import serializers
from . models import Info

class InfoSerializer(serializers.ModelSerializer):
   class Meta: 
      model=Info
      fields =['country_name','cases','test_completed','deaths','date_update','vaccine_total_doses']