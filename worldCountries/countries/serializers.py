from django.db.models import fields
from rest_framework import serializers
from .models import Countries

class CountriessSerializer(serializers.ModelSerializer):

    class Meta:
        model = Countries
        fields=('id','name','capital')
