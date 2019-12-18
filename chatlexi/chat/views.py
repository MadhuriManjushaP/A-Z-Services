
from django.shortcuts import render,redirect
from django.db import models
from chat.models import UserDetails
from django.template import loader
from django.http import HttpResponse
from django.forms import modelformset_factory
import random

# Create your views here.

from .forms import UserModelForm     #importing the form                            

def userDetails(request):

    if request.method == 'POST':
        form = UserModelForm(request.POST)
        if form.is_valid():


            u = form.save()
            users = UserDetails.objects.latest('name')  #the last name in the database
            last_name = users.name
            formView(request)     #calling the session function
           #Calculating BMI for  the user for knowing the chances of the user getting the hypo and hyper since the weight plays an impoertant role
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
            

 #To display the greetings randomly for every different user that logs in to the chat page(temp.html)
            res=["may i know ur problem","how are you feeling today","since you visited us we can  understand that something is bothering today, may i know your symtoms"]
            res1 = random.choice(res)
                
            return render(request, 'temp.html', {'last_name': last_name,'res1':res1,'bmi': bmi,'a': a})
            
    else: 
        form_class = UserModelForm

    return render(request, 'new.html', {
        'form': form_class, })
#creating a session for the new.html after user enters the details and clicked on submit button.
def formView(request):
    request.session['users'] = 'users'     #creates a session 'users'
    if request.session.has_key('users'):
       users=request.session['users']      #if the sessionID already has a key it is assigned to user
       #request.session['last_activity'] = datetime.now()
       return render(request, 'temp.html', {})
    else:
        logout(request)
        return render(request, 'logout.html', {"users":users})

# To delete the session when logout view has been called
def logout(request):                   
    if request.session.has_key('users'):       
        del request.session['users']
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
        

        response_data['title'] = title                                #the title(the field where user types) is stored in this response dictionary 
       
      
        Post.objects.create(                                            #creating a new object and sending it to title field which is stored in db everytime user  clicks on send
            title = title,
           
            )
        return JsonResponse(response_data)                       

    return render(request, 'temp.html', {'posts':posts})    
