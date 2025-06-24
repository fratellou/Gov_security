from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from accounts.models import Message


@login_required
def home_view(request):
    user_department = request.user.department
    messages = Message.objects.filter(department=user_department).order_by('timestamp')[:100]
    return render(request, "home/home.html", {"messages": messages})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def post_message(request):
    if request.method == 'POST':
        message_text = request.POST.get('message_text')
        if message_text:  # Проверка на пустое сообщение
            new_message = Message.objects.create(
                department=request.user.department,
                author=request.user,
                message_text=message_text
            )
            return redirect('home')
        else:
            return render(request, 'home/home.html', {'error': "The message can’t be empty."})
    return redirect('home')
