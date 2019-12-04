
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
            Height = users.height
            Height_1 = Height/100
            Weight = users.weight
            bmi=round(Weight / (Height_1 * Height_1), 2)
            if bmi<18.5:
                a="Underweight"
            elif bmi>18.5 and bmi<24.9:
                a="normal weight"
            elif bmi>=25 and bmi<29.9:
                a="over weight"
            elif bmi>=30 and bmi<40:
                a="obesity"
            elif bmi>=40:
                a="Extreme obesity"
            

            #user_visits = request.session.get('user_visits', 0)
            #request.session['user_visits'] = user_visits + 1
            #request.session['users'] = users
            #request.session['users.name'] = 'username'
            res=["may i know ur problem","how are you feeling today","since you visited us we can  understand that something is bothering today, may i know your symtoms"]
            res1 = random.choice(res)
                
            return render(request, 'temp.html', {'last_name': last_name,'res1':res1,'bmi': bmi,'a': a})
            
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
#new form 
from django.shortcuts import render
from django.http import JsonResponse
from .models import Post

def create_post(request):
    posts = Post.objects.all()
    response_data = {}

    if request.POST.get('action') == 'post':
        title = request.POST.get('title')
        #description = request.POST.get('description')

        response_data['title'] = title
        #response_data['description'] = description
      
        Post.objects.create(
            title = title,
            #description = description,
            )
        return JsonResponse(response_data)

    return render(request, 'temp.html', {'posts':posts})    