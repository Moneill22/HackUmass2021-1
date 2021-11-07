from django.urls import path
from . import views
from companies.views import company_profile_view, d3_api_view

urlpatterns = [
    path('', views.index, name='index'),
    # path('signup', views.signup),
    # path('signin', views.signin),
    path('dashboard/<str:username>', views.dashboard, name='dashboard'),
    path('update_dashboard/<str:username>', views.update_dashboard, name='dashboard'),
    path('company/<str:name>', company_profile_view),
    path('apiGraph/<str:name>', d3_api_view)
]