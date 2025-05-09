from django.contrib import admin

# Register your models here.

from .models import User, Event, RouteTrack, EventParticipation, ClubCard



class UserModelAdmin(admin.ModelAdmin):
    list_filter=['first_name', 'last_name','user_type']
    search_fields=['first_name', 'last_name','user_type','phone','email']
    list_display = ['first_name', 'last_name', 'user_type', 'email']
    class Meta:
        model = User

class EventParticipationInline(admin.TabularInline):
    model = EventParticipation
    
class EventModelAdmin(admin.ModelAdmin):
    list_filter=['event_type','status','difficulty','price']
    search_fields=['event_type','name']
    list_display=['event_type','status','difficulty','price','name','planned_date']
    ordering=['planned_date']
    inlines = [EventParticipationInline]
    class Meta:
        model = Event

class RouteTrackAdmin(admin.ModelAdmin):
    list_filter=['event','name','distance']
    search_fields=['event','name','distance']
    list_display=['event','name','distance']
    class Meta:
        model = RouteTrack

class ClubCardAdmin(admin.ModelAdmin):
    list_filter=['state','number','sale_date']
    search_fields=['owner__first_name','owner__last_name','number']
    list_display=['owner','state','number','sale_date']
    class Meta:
        model = ClubCard




admin.site.register(User, UserModelAdmin)
admin.site.register(Event, EventModelAdmin)
admin.site.register(RouteTrack, RouteTrackAdmin)
admin.site.register(ClubCard, ClubCardAdmin)
