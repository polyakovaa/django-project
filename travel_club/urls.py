from django.urls import path, re_path
from . import views as travel_views

urlpatterns=[
    path('home/', travel_views.home, name='home'),
    path('events/',travel_views.events,name='events'),
    path('events/date/<str:date>/', travel_views.events_by_date, name='events_by_date'),
    re_path(r'^events/(?P<event_id>\d+)/participants/$', travel_views.event_participants, name='event_participants'),
    re_path(r'^events/(?P<event_id>\d+)/detail/$', travel_views.detail, name='detail'),
    path('event_types/', travel_views.event_types, name='event_types'),
    path('event_types/<str:type>/', travel_views.events_by_type, name='events_by_type'),
]

