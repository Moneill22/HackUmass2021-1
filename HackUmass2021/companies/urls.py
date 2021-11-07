from django.urls import path

from .views import company_profile_view


urlpatterns = [
    path('company/<str:company_id>', company_profile_view),
]