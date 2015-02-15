from django.shortcuts import render
from django.shortcuts import render_to_response
from serializers import RentSerializer
from permissions import IsOwnerReadOnly
from rest_framework import viewsets
from models import Equipment

class RentViewSet(viewsets.ModelViewSet):

	queryset = Equipment.objects.all()
	serializer_class = RentSerializer
#	permission_classes = (IsOwnerReadOnly,)

#	def pre_save(self, obj):
#		obj.owner = self.request.user

