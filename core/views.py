from django import urls
from django.http import request
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Pet
# Create your views here.


@login_required(login_url='/login/')
def register_pet(request):
    pet_id = request.GET.get('id')
    if pet_id:
        pet = Pet.objects.get(id=pet_id)
        if pet.usuário == request.user:
            return render(request, 'register-pet.html', {'pet': pet})
    return render(request, 'register-pet.html')


@login_required(login_url='/login/')
def delete_pet(request, id):
    pet = Pet.objects.get(id=id)
    if pet.usuário == request.user:
        pet.delete()
    return redirect('/')


@login_required(login_url='/login/')
def set_pet(request):
    cidade = request.POST.get('cidade')
    email = request.POST.get('email')
    telefone = request.POST.get('telefone')
    descrição = request.POST.get('descrição')
    foto = request.FILES.get('file')
    pet_id = request.POST.get('pet-id')
    if pet_id:
        pet = Pet.objects.get(id=pet-id)
        if usuário == pet.usuário:
            pet.email = email
            pet.telefone = telefone
            pet.cidade = cidade
            pet.descrição = descrição
            if foto:
                pet.foto = foto
            pet.save()
    else:
        usuário = request.user
        pet = Pet.objects.create(email=email, cidade=cidade, telefone=telefone,
                                 foto=foto, usuário=usuário, descrição=descrição)
    url = f'/pet/detail/{pet.id}/'
    return redirect(url)


@login_required(login_url='/login/')
def list_all_pets(request):
    pet = Pet.objects.filter(ativo=True)
    return render(request, 'list.html', {'pet': pet})


def list_user_pets(request):
    pet = Pet.objects.filter(ativo=True, usuário=request.user)
    return render(request, 'list.html', {'pet': pet})


@login_required(login_url='/login/')
def pet_detalhes(request, id):
    pet = Pet.objects.get(ativo=True, id=id)
    return render(request, 'pet.html', {'pet': pet})


def logout_user(request):
    print(request.user)
    logout(request)
    return redirect('/login/')


def login_user(request):
    return render(request, 'login.html')


@csrf_protect
def submit_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        next = request.POST.get('next')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if next:
                messages.success(request, 'Logado com Suecesso!')
                return redirect(next)
            else:
                messages.success(request, 'Logado com Suecesso!')
                return redirect('/')
        else:
            messages.error(
                request, 'Usuário e senha Inválidos. Favor Tente novamente')
            return redirect('/login')
    else:
        return render(request, '/login/')
