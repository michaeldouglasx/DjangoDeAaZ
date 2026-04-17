from django.urls import path

from medicSearch.views.ProfileView import list_profile_view

urlpatterns = [
    path("", list_profile_view, name= 'list_profile'),
    path("<int:id>/", list_profile_view, name='list_profile_detail'),
]