from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from accounts.models import Permission
from profiles.models import Employee
from resources.models import Resource


@login_required
def resources_list(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    resources = None
    if hasattr(employee, 'position'):
        permissions = Permission.objects.filter(
            position=employee.position).select_related('resource')
        resources = [permission.resource for permission in permissions]
    return render(request, 'resources/resources.html', {
        'resources': resources,
        'employee': employee
    })


@login_required
def download_resource(request, resource_id):
    resource = get_object_or_404(Resource, id=resource_id)

    response = HttpResponse(resource.resource_file,
                            content_type='application/force - download')
    response[
        'Content-Disposition'] = 'attachment;' \
        f'filename ="{resource.resource_file.name.split("/")[-1]}"'

    return response
