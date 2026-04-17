from medicSearch.views import *

from django.urls import path, include

app_name = 'medicSearch'

urlpatterns = [
    path('', include('medicSearch.urls.HomeUrls')),
    path('profile/', include('medicSearch.urls.ProfileUrls')),
]
