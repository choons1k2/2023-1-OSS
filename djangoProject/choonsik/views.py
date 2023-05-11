# views.py
from django.shortcuts import render, redirect
from .models import Create
from .form import CreateForm

def home(request):
    return render(request, 'home.html')

def free_board(request):
    posts = Create.objects.all()
    return render(request, 'free_board.html', {'posts': posts})

def new_post(request):
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.isValid():
            form.save()
            return redirect('choonsik:free_board')
    else:
        form = CreateForm()
    return render(request, 'new_post.html', {'form': form})
