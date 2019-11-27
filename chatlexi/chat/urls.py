from django.urls import path
from django.contrib import admin

from . import views as chat_views

urlpatterns = [
 path('', chat_views.userDetails),
 path('test/', chat_views.userDetails),
 path('create/', chat_views.create_session),

 path('logout/', chat_views.logout)
 
    
    
]
