from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50,required=False,help_text='Optional')
    last_name = forms.CharField(max_length=50,required=False,help_text='Optional')

    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2']
        
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Display name"
        self.fields["email"].label = "Email address"