from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterFrom
from .forms import MediaSelectionForm
import os
from newsapi import NewsApiClient
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterFrom(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}.')
            return redirect('login')
    else:
        form = UserRegisterFrom()
    return render(request, 'users/register.html', {'form':form})

# Creating the form to allow users to select the news that they want to see displayed on their personal homepage

@login_required
def mediaselction(request):

    if request.method == 'POST':
            form = MediaSelectionForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user =request.user
                instance.save()
                messages.success(request, f'Your favorites media have beeen saved.')
                return redirect('home')
    else:
        form = MediaSelectionForm()



    return render(request, 'users/media_selection_form.html', {'form':form})