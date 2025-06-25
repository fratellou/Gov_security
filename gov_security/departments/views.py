from django.shortcuts import render, get_object_or_404
from profiles.models import Employee
from departments.models import Department
from django.contrib.auth.decorators import login_required


@login_required
def department_info(request, department_id):
    department = get_object_or_404(Department, pk=department_id)
    employee = None
    if request.user.is_authenticated:
        try:
            employee = Employee.objects.get(username=request.user.username)
        except Employee.DoesNotExist:
            employee = None
    return render(request, 'departments/department.html', {
        'department': department,
        'employee': employee
    })
