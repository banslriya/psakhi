from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name='home'
urlpatterns=[
		path('',TemplateView.as_view(template_name='home/index.html'),name='home'),
		path('about-us/',TemplateView.as_view(template_name='home/about.html'),name='about'),
		path('services/',views.services,name='services'),
		path('support_us/',views.support_us,name='support_us'),
]
