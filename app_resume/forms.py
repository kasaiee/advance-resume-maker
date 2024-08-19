from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from app_resume.models import Resume, Education

# User = get_user_model()

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        exclude = ['user']


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        # fields = '__all__'
        exclude = ['user']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        # exclude = ['password', 'last_login']
