from django.urls import path
from . import views

urlpatterns = [
    path('api/companies', views.CompanyList.as_view(), name='company_list'), # api/contacts will be routed to the CompanyList view for handling
    path('api/companies/<int:pk>', views.CompanyDetail.as_view(), name='company_detail'), # api/contacts will be routed to the CompanyDetail view for handling
]