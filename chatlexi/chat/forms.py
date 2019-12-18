from django.forms import ModelForm
from chat.models import UserDetails
#create form class and fields here for user registration
class UserModelForm(ModelForm):
    class Meta:
        model = UserDetails
        fields = ['name','age','gender','height','weight','smoke','drink','diabetes','highbp']
 
