from django.forms import ModelForm
from chat.models import UserDetails

class UserModelForm(ModelForm):
    class Meta:
        model = UserDetails
        fields = ['name','age','gender','height','weight','smoke','drink','diabetes','highbp']
 