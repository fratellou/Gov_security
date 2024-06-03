from django.shortcuts import render, get_object_or_404
from accounts.models import Employee


def tasks_list(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    return render(request, 'tasks/tasks.html', {'employee': employee})
