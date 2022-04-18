from django.urls import path

from rent_property.Views import AppartmentView, ContactUsView

urlpatterns = [
    path('apartment', AppartmentView.ApartmentView.as_view(), name='ApartmentView'),
    path('apartment_list', AppartmentView.ApartmentListView.as_view(), name='ApartmentListView'),
    path('apartment/<int:pk>', AppartmentView.ApartmrntDetailedView.as_view(), name='ApartmrntDetailedView'),
    path('contact', ContactUsView.ContactUsView.as_view(), name='ContactUsView'),
    path('contact/<int:pk>', ContactUsView.ContactUsDetailedView.as_view(), name='ContactUsDetailedView'),
    path('/', ContactUsView.ContactUsDetailedView.as_view(), name='ContactUsDetailedView'),

]
