from django.contrib import admin
from .models import Destination, TravelPlan, Review

admin.site.site_header = "Tourism Admin Panel"
admin.site.site_title = "Tourism Admin"
admin.site.index_title = "Welcome to Tourism System"


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_popular')
    list_editable = ('is_popular',)


@admin.register(TravelPlan)
class TravelPlanAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'travel_date')


# ✅ NEW
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'destination', 'rating')