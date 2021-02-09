


# menu/urls.py
from django.urls import path

from . import views

urlpatterns = [
	#Empty or blank URL
	# localhost:8000/
	path('', views.homemenu, name='myhome'),
	path('login/', views.loginmenu, name='mylogin'),
	path('register/', views.registermenu, name='register'),
	path('logout/', views.logoutmenu, name='logoutURL'),
]
