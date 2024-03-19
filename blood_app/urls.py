from django.urls import path
from .views import BloodEventView,DonorListView
urlpatterns=[
    path('blood_event/',BloodEventView.as_view(),name='blood_event'),
    path('donor_list/', DonorListView.as_view(),name='donor_list')
]