from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import ResourceType, Resource, Position, Permission, Department, Head, Task, Employee, TaskList


class EmployeeAdmin(BaseUserAdmin):

    model = Employee
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'patronymic', 'email', 'age', 'phone')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (('Relations'), {'fields': ('position', 'department')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'first_name', 'last_name', 'patronymic', 'email',  'age', 'phone', 'is_active', 'is_staff', 'position', 'department'),
        }),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'patronymic', 'age', 'phone', 'position', 'department')
    search_fields = ('username', 'first_name', 'last_name', 'patronymic', 'email',  'phone')
    ordering = ('username',)


admin.site.register(ResourceType)
admin.site.register(Resource)
admin.site.register(Position)
admin.site.register(Permission)
admin.site.register(Department)
admin.site.register(Head)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Task)
admin.site.register(TaskList)

