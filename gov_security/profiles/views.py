from django.shortcuts import render, get_object_or_404
from profiles.models import Employee
from django.contrib.auth.decorators import login_required
# from django.http import HttpResponseRedirect


@login_required
def employee_profile(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    return render(request, 'profiles/profile.html', {'employee': employee})
