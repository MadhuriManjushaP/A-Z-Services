
from django.shortcuts import render,redirect
from django.db import models
from chat.models import UserDetails
from django.template import loader
from django.http import HttpResponse
from django.forms import modelformset_factory
import random

# Create your views here.

from .forms import UserModelForm

def userDetails(request):

    if request.method == 'POST':
        form = UserModelForm(request.POST)
        if form.is_valid():


            u = form.save()
            users = UserDetails.objects.latest('name')
            last_name = users.name
            user_visits = request.session.get('user_visits', 0)
            request.session['user_visits'] = user_visits + 1
            #request.session['users'] = users
            #request.session['users.name'] = 'username'
            res=["may i know ur problem","how are you feeling today","since you visited us we can  understand that something is bothering today, may i know your symtoms"]
            res1 = random.choice(res)
                
            return render(request, 'test.html', {'last_name': last_name,'res1':res1})
            
          
    else: 
        form_class = UserModelForm

    return render(request, 'new.html', {
        'form': form_class, })

'''def logout(request):
    {
      
      del request.session['users']
      return HttpResponse("<strong>You are logged out.</strong>")
    } '''
'''def logout(request):
        return redirect('/userdetails/')'''
def create_session(request):
    request.session['users.name'] = 'username'
    return HttpResponse("<h1>dataflair<br> the session is set</h1>")
'''def logout(request):
        
        del request.session['users.name']
        return HttpResponse("<h1>You are Logged out.Thank you for using our Chatbot</h1>")'''

def logout(request):
    return render(request,'logout.html')
