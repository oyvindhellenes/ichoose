from django.db import models
from django.utils import timezone
import datetime

class Equipment(models.Model):
	type = models.CharField(max_length=100)
	description = models.CharField(max_length=300)
	location = models.CharField(max_length=100)

	def __str__(self):
		return self.type

class Reservation(models.Model):
	equipment = models.ForeignKey(Equipment)
	from_time = models.DateTimeField('From:')
	to_time = models.DateTimeField('To:')
	reserved_by = models.CharField(max_length=100)
	comment = models.CharField(max_length=200)

	def __str__(self):
		return self.equipment.type + " reserved by " +  self.reserved_by

