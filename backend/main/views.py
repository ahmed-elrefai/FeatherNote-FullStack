from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login,logout as auth_logout
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Note

# Create your views here.

def homePage(request):
    if request.user.is_authenticated:
        logout(request)
    return render(request, 'index.html')

def login(request, user=None):
    if request.user.is_authenticated:
        logout(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)  
    if user:
        auth_login(request, user)
        return redirect(reverse('dashboard'))

    return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    return redirect('homepage')

def signup(request):
    if request.user.is_authenticated:
        logout(request)
    if request.method == 'POST':
        data = request.POST
        user = User.objects.create_user(username=data['username'], email=data['email'] ,password=data['password'])
        response = login(request, user)
        return response
    
    return render(request, 'signup.html')

def deleteNote(request, note_id):
    if request.method == 'POST':
        note = get_object_or_404(Note, pk=note_id)
        note.delete()
    return redirect('dashboard')

def dashboard(request):
    notes = Note.objects.filter(author=request.user)
    return render(request, 'dashboard.html', context={'user':request.user, 'notes':notes})

def displayNote(request, note_id=None):
    if request.method == 'GET':
        if note_id:
            note = Note.objects.filter(author=request.user, id=note_id).get()
            
            return render(request, 'note.html', context={'note':note})
        else:
            return render(request, 'note.html')
    elif request.method == 'POST':
        new_title = request.POST['title']
        new_content = request.POST['content']
        user_id = request.user.id
        if note_id:
            note = Note.objects.filter(id=note_id).get()
            note.title=new_title 
            note.content=new_content
            note.save()
        else:
            note = Note(title=new_title, content=new_content,author_id=user_id)
            note.save()
        return redirect('dashboard')
    
def custom_404_view(request, exception):
    return render(request, '404.html', status=404)