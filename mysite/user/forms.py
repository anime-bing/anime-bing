from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.forms.widgets import FileInput
from django.contrib.auth.forms import AuthenticationForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'                @gmail.com','id':'reg-fields','class':'reg-email'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':' username','id':'reg-fields','class':'reg-user'}))
    # password1 = forms.CharField(widget=forms.PasswordInput(attrs={'id':'reg-fields'}))
    # password2 = forms.CharField(widget = forms.PasswordInput(attrs={'id':'reg-pw2'}))
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class ProfileEditForm(forms.ModelForm):
    profilepic = forms.FileField(label="",widget=forms.ClearableFileInput(attrs={'id':'profile-pic-changer'}))
    class Meta:
        model= Profile
        fields = ['profilepic']

class UserEditForm(forms.ModelForm):
    email = forms.EmailField(label="",widget=forms.EmailInput(attrs={'id':'profile-pic-changer'}))
    class Meta:
        model = User
        fields = ['email']

class UserLoginForm(forms.Form):
    username = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'login-un-form','placeholder':'Username','row':'2','col':'40'}))
    password = forms.CharField(label="",widget=forms.PasswordInput(attrs={'class':'login-pw-form','placeholder':'Password'}))
