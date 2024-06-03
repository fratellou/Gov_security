from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomAuthForm


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Перенаправление на главную после успешного входа
        else:
            form.errors.clear()
            form.add_error(None, 'Введены неправильное имя пользователя или пароль. Повторите попытку.')
    else:
        form = CustomAuthForm()
    return render(request, 'accounts/login.html', {'form': form})
