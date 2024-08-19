from datetime import datetime
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from app_resume.forms import ProfileForm, ResumeForm, EducationForm
from django.forms import modelformset_factory


def index(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username, password)
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
    return render(request, 'index.html')


def edit_profile(request):
    context = {}
    if request.method == 'POST':
        form = ProfileForm(instance=request.user, data=request.POST)
        resume_form = ResumeForm(instance=request.user.resume, data=request.POST, files=request.FILES)
        if form.is_valid() and resume_form.is_valid():
            form.save()
            resume_form.save()
        context['form'] = form
        context['resume_form'] = resume_form

        titles = request.POST.getlist('title')
        descriptions = request.POST.getlist('description')
        for index, title in enumerate(titles):
            education_form = EducationForm(data={
                'title': title,
                'description': descriptions[index],
            })
            if education_form.is_valid():
                education_form.save()
    else:
        context['education_form'] = EducationForm()
        context['form'] = ProfileForm(instance=request.user)
        context['resume_form'] = ResumeForm(instance=request.user.resume)
    return render(request, 'edit-profile.html', context)
