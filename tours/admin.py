from django.contrib import admin
from tours.models import Tour, RegularToure
# Register your models here.


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ["title", "price", "created", "updated" ,"is_active"]
    list_filter = ["created", "is_active", "price"]
    search_fields = ["title", "created", "description"]
    list_aditable = ["is_active", "price"]

@admin.register(RegularToure)
class Regular(admin.ModelAdmin):
    list_dispaly = ['tour.title', 'start', 'end', 'places_count', 'status']
    list_filter = ['start', 'end', 'status']
    seach_fields = ['tour__title', 'start', 'end']
    list_editabe = ['status', 'start', 'end', 'palaces_count']