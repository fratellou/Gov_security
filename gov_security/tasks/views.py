from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from profiles.models import Employee


@login_required
def tasks_list(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    return render(request, 'tasks/tasks.html', {'employee': employee})
