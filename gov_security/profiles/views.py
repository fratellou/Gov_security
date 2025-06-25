from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from profiles.models import Employee


@login_required
def employee_profile(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    return render(request, 'profiles/profile.html', {'employee': employee})
