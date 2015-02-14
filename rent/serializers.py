from rest_framework import serializers
from rent.models import Equipment
from django.contrib.auth.models import User

class RentSerializer(serializers.HyperlinkedModelSerializer):
	class meta:
		model = Equipment
		fields = ('type')
		