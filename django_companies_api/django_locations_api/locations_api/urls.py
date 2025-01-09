from django.urls import path
from . import views

urlpatterns = [
    path('api/locations', views.LocationtList.as_view(), name='location_list'), # api/locations will be routed to the LocationList view for handling
    path('api/locations/<int:pk>', views.LocationDetail.as_view(), name='location_detail'), # api/contacts will be routed to the LocationDetail view for handling
]