from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import Permission
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.contrib.auth import logout

# Create your views here.


class RegisterView(View):
    template_name = 'register.html'

    def get(self, request):
        form = UserCreationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            visualizar_permiso = Permission.objects.get(codename='visualizar_catalogo')
            user.user_permissions.add(visualizar_permiso)
            messages.success(request, '¡Registro exitoso!')
            return redirect('index')
        return render(request, self.template_name, {'form': form})
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')