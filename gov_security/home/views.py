from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from home.models import Message


@login_required
def home_view(request):
    user_department = request.user.department
    messages = Message.objects.filter(
        department=user_department).order_by('timestamp')[:100]
    context = {
        'messages': messages,
        'department_name': user_department.department_name
    }
    return render(request, 'home/home.html',  context)


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def post_message(request):
    user_department = request.user.department
    messages = Message.objects.filter(
        department=user_department).order_by('timestamp')[:100]

    if request.method == 'POST':
        message_text = request.POST.get('message_text')
        if message_text:
            Message.objects.create(
                department=request.user.department,
                author=request.user,
                message_text=message_text
            )
            return redirect('home')
        else:
            context = {
                'messages': messages,
                'error': "The message can't be empty."
            }
            return render(request, 'home/home.html', context)

    context = {'messages': messages}
    return render(request, 'home/home.html', context)
