from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class UserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'placeholder':'john_doe'
        })
        self.fields['email'].widget.attrs.update({
            'placeholder': 'johndoe@gmail.com'
        })
        self.fields['first_name'].widget.attrs.update({
            'placeholder': 'John'
        })
        self.fields['last_name'].widget.attrs.update({
            'placeholder': 'Doe'
        })
        self.fields['password1'].widget.attrs.update({
            'placeholder': '***********'
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder': '***********'
        })



    email = forms.EmailField()
    first_name = forms.CharField(max_length=50, required=False)
    last_name = forms.CharField(max_length=50, required=False)

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email','password1', 'password2']
