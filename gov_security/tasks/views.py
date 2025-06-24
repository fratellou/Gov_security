from django.shortcuts import render, get_object_or_404
from accounts.models import Employee
from django.contrib.auth.decorators import login_required


@login_required
def tasks_list(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    return render(request, 'tasks/tasks.html', {'employee': employee})
