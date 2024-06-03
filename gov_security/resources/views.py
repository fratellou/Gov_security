from django.shortcuts import render, get_object_or_404
from accounts.models import Employee, Permission


def resources_list(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    resources = None
    if hasattr(employee, 'position'):
        permissions = Permission.objects.filter(position=employee.position).select_related('resource')
        resources = [permission.resource for permission in permissions]
    return render(request, 'resources/resources.html', {
        'resources': resources,
        'employee': employee
    })
