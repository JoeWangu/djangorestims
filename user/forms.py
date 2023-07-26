from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from user.models import User

#create a class for the form
class UserForm(UserCreationForm):
    error_messages = {
        "password_mismatch": ("The two password fields didn’t match."),
    }
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        def clean_password2(self):
            password1 = self.cleaned_data.get('password1') # type: ignore
            password2 = self.cleaned_data.get('password2') # type: ignore
            if password1 and password2 and password1 != password2:
                raise ValidationError(
                self.error_messages["password_mismatch"], # type: ignore
                code="password_mismatch",
            )
                # raise forms.ValidationError("Passwords don't match")
            return password2
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'input-field', 'id': 'username})', 'autofocus': True})
    )
    # password = forms.CharField(
    #     widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'input-field', 'id': 'password', 'autocomplete': 'current-password'})
    # )

    # get the original then update to add attributes
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget.attrs.update({'placeholder': 'Password', 'class': 'input-field', 'id': 'password'})