from django.urls import path
from django.contrib import admin
#import views here
from . import views as chat_views
#create path urls here
urlpatterns = [
 path('', chat_views.userDetails),
 path('temp/', chat_views.userDetails),
 path('session/', chat_views.create_session),
path('create/', chat_views.create_post, name="create"),
path('logout/', chat_views.logout)
 
    
    
]
