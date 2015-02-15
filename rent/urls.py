from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rent import views

urlpatterns = [
	url(r'^equipment/$', views.RentList.as_view()),
	url(r'^equipment/(?P<pk>[0-9]+)/$', views.RentDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)