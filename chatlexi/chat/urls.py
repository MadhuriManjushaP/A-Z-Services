from django.urls import path
from django.contrib import admin

from . import views as chat_views

urlpatterns = [
 path('', chat_views.userDetails),
 path('temp/', chat_views.userDetails),
 path('session/', chat_views.create_session),
path('create/', chat_views.create_post, name="create"),
path('logout/', chat_views.logout)
 
    
    
]
