from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from image_rest.views import *

urlpatterns = [
    url(r'^images/$', ImageList.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns = format_suffix_patterns(urlpatterns)

