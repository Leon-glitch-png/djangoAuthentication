from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from django.contrib.auth.models import User
from django import forms
from .validators import allow_only_gmail

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True,validators=[allow_only_gmail],label="Email" ,help_text="Required. Enter a valid gmail address.",)
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            common_classes = "form-control mb-2 mt-2 p-2 rounded border border-gray-300"

            for field in self.fields.values():
                field.widget.attrs.update({"class": common_classes})
        
        
class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            common_classes = "form-control mb-2 mt-2 p-2 rounded border border-gray-300"

            for field in self.fields.values():
                field.widget.attrs.update({"class": common_classes})
                
            self.fields['username'].widget.attrs.update({'placeholder': 'Username'})
            self.fields['password'].widget.attrs.update({'placeholder': 'Password'})
            
            self.fields['username'].label = 'Username'
            self.fields['password'].label = 'Password'
            
            
class CustomPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            common_classes = "form-control mb-2 mt-2 p-2 rounded border border-gray-300"

            for field in self.fields.values():
                field.widget.attrs.update({"class": common_classes})
                
            self.fields['email'].widget.attrs.update({'placeholder': 'Enter your email address'})
            self.fields['email'].label = 'Email Address'