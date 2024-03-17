from django.urls import path
from .views import BloodEventView
urlpatterns=[
    path('blood_event/',BloodEventView.as_view(),name='blood_event')
]