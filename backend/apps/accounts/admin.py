from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User

admin.site.site_header = 'Trails App'
admin.site.site_title = 'Administration Portal'
admin.site.index_title = 'Trails App'


@admin.register(User)
class UserAdmin(BaseUserAdmin):

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        (
            'Permissions',
            {
                'fields': (
                    'is_active',
                    'email_verified',
                    'is_superuser',
                ),
            },
        ),
        ('Important dates', {'fields': ('last_login', 'created_at')}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2'),
            },
        ),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'created_at')
    list_filter = ('is_active',)
    ordering = ('email', 'is_active', 'created_at')
    search_fields = ('first_name', 'last_name', 'email')
    readonly_fields = ('created_at', 'updated_at', 'last_login')
