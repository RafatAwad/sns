from django.forms import ModelForm, TextInput, FileInput, Form, CharField, PasswordInput
from .models import UserProfile, User
from django.utils.translation import gettext as _

class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'



#class UserInfoForm(ModelForm):

class AdminLoginForm(Form):
    username = CharField(
        widget= TextInput(
            attrs={
                "placeholder": _("username"),
                "class": "form-control"
            }
        ))
    password = CharField(
        widget=PasswordInput(
            attrs={
                "placeholder": _("Password"),
                "class": "form-control"
            }
        ))


  