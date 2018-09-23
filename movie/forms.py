from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Movie, Profile

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'genre', 'director', 'rating']

class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True

    gender_choices = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    
    birthdate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'})) 
    gender = forms.ChoiceField(widget=forms.Select, choices=gender_choices)
    address = forms.CharField(max_length=50, widget=forms.Textarea)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'birthdate', 'gender', 'address', 'email', 'username', 'password1', 'password2']
        