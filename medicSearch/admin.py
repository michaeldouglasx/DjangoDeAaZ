from django.contrib import admin
from .models import *

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('user', 'role', 'birth')
    empty_value_display = '-'
    list_display_links = ('user', 'role')
    list_filter = ('user__is_active',)
    readonly_fields = ('user',)
    fields = ('user','role', 'image', 'birthday','specialties', 'addresses' )
    ordering = ['user']
    search_fields = ('user__username',)

    def birth(self, obj):
        if obj.birthday:
            return obj.birthday.strftime('%d/%m/%Y')



@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    fields = ()
    empty_value_display = '-'

@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    fields = ()
    empty_value_display = '-'

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    fields = ()
    empty_value_display = '-'


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    fields = ()
    empty_value_display = '-'

@admin.register(DayWeek)
class DayWeekAdmin(admin.ModelAdmin):
    fields = ()
    empty_value_display = '-'

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    fields = ()
    empty_value_display = '-'

@admin.register(Neighborhood)
class NeighborhoodAdmin(admin.ModelAdmin):
    fields = ()
    empty_value_display = '-'
