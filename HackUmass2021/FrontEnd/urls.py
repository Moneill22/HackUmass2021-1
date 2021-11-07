from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('signup', views.signup),
    # path('signin', views.signin),
    path('dashboard/<str:username>', views.dashboard, name='dashboard'),
    path('update_dashboard/<str:username>', views.update_dashboard, name='dashboard')
]