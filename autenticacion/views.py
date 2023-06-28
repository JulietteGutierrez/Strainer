from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm

class VRegistro(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("inicio")
    template_name = "registro/registro.html"

def cerrar_sesion(request):
     logout(request)
     return redirect("inicio")

def logear(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get("username")
            contra=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre_usuario,password=contra)
            if usuario is not None:
                login(request,usuario)
                return redirect("inicio")
            else:
                messages.error(request, "usuario no valido")
        else:
            messages.error(request, "Informacion incorrecta")   
             
    form=AuthenticationForm()
    return render(request,"login/login.html", {"form":form})







# class VRegistro(View):
    
#     def get(self, request):
#         form = Registroform
#         # form=UserCreationForm()
#         return render(request,"registro/registro.html", {"form":form})

#     def post(self, request):
#         form=Registroform(request.POST)
#         # form=UserCreationForm(request.POST)

#         if form.is_valid():
#             usuario=form.save()
            
#             login(request , usuario)
            
#             return redirect("inicio")
        
#         else:
#             for msg in form.error_messages:
#                 messages.error(request , form.error_messages[msg])
            
#             return render(request,"registro/registro.html", {"form":form})

# def cerrar_sesion(request):
#     logout(request)
#     return redirect("inicio")

# def logear(request):
#     if request.method=="POST":
#         form=AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             nombre_usuario=form.cleaned_data.get("username")
#             contra=form.cleaned_data.get("password")
#             usuario=authenticate(username=nombre_usuario,password=contra)
#             if usuario is not None:
#                 login(request,usuario)
#                 return redirect("inicio")
#             else:
#                 messages.error(request, "usuario no valido")
#         else:
#             messages.error(request, "Informacion incorrecta")   
             
#     form=AuthenticationForm()
#     return render(request,"login/login.html", {"form":form})










