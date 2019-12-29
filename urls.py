from django.urls import path
from django.contrib import admin

from . import views as detailsapp_views
# passing views to urls and setting uls path
urlpatterns = [
 path('userdetails/', detailsapp_views.userDetails),
 path('test/', detailsapp_views.userDetails),

path('', admin.site.urls),
]
urlpatterns = [
    path('crudops/', detailsapp_views.crudops, name='crudops')
]
urlpatterns = [
    path('crudops1/',detailsapp_views.crudops1, name='crudops1')
]
urlpatterns = [
    path('crudops2/',detailsapp_views.crudops1, name='crudops2')
]
urlpatterns = [
    path('crudops3/',detailsapp_views.crudops1, name='crudops3')
]
urlpatterns = [
    path('crudops4/',detailsapp_views.crudops1, name='crudops4')
]