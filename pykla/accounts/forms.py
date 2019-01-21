from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class RegForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = [
            'username','first_name','last_name','email','password1', 'password2'
        ]

        def save(self, commit=True):
            user = super(RegForm, self).save(commit=False)
            user.first_name = forms.cleaned_data('first_name')
            user.last_name = forms.cleaned_data('last_name')
            user.email = forms.cleaned_data('email')


            if commit:
                user.save()

            return user

#edit user profile
class EditProfile(UserChangeForm):
    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name','password'
        ]
