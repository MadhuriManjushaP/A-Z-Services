from django.urls import path
from django.contrib import admin

from . import views as chat_views

urlpatterns = [
 path('userdetails/', chat_views.userDetails),
 path('test/', chat_views.userDetails),
 path('create/', chat_views.create_session),
 path('', admin.site.urls),
 path('logout/', chat_views.logout)
 
    
    
]
