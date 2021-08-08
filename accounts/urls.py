from django.urls import path
from .import views

app_name='accounts'

urlpatterns = [

    path("booking",views.booking,name='booking'),




]