from django.conf.urls import *
from rest_framework import routers
from rent import views

router = routers.DefaultRouter()
router.register(r'rent', views.RentViewSet)

urlpatterns = patterns('', 
						url(r'^api/', include(router.urls)),
						)