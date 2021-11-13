from rest_framework import serializers
from .models import Hotel

class HotelSerializer(serializers.ModelSerializer):
	class Meta:
		model = Hotel
		fields = ('id', 'name', 'provider', 'rating', 'review', 'price', 'city', 'checkin', 'checkout')