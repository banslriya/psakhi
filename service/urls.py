from django.urls import path
from . import views

app_name = 'service'

urlpatterns = [
    path('',views.service,name='service'),
    path('donate',views.donate_medicine, name='donate_medicine'),
    path('create-stock',views.drug_stock, name='create_stock'),
    path('check-assignment',views.check_assignment, name='check_assignment'),
	path('assign-volunteer',views.assign_volunteer, name='assign_volunteer'),
]
