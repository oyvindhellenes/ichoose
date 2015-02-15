from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import Http404

from serializers import RentSerializer
from permissions import IsOwnerReadOnly
from rest_framework import viewsets
from models import Equipment

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status



class RentList(APIView):

	def get(self, request, format=None):
		equips = Equipment.objects.all()
		serializer = RentSerializer(equips, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = RentSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RentDetail(APIView):

	def get_object(self, pk):
		try:
			return Equipment.objects.get(pk=pk)
		except Equipment.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		equipment = self.get_object(pk)
		serializer = RentSerializer(equipment)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		equipment = self.get_object(pk)
		serializer = RentSerializer(equipment, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		equipment = self.get_object(pk)
		equipment.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

