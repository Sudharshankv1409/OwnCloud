from django.urls import path
from . import views
app_name = 'cloud'

urlpatterns = [
    path('',views.CloudHomePage.as_view(),name = 'home'),
]