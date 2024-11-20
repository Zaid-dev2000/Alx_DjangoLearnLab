from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser  # Import your CustomUser model

class CustomUserAdmin(UserAdmin):
    # Customizing the admin interface for your CustomUser model
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active')  # Customize fields to display
    list_filter = ('is_staff', 'is_active')           # Filters in the admin interface
    fieldsets = (                                     # Fields shown in the edit form
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (                                 # Fields shown in the add form
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)                        # Fields to search by
    ordering = ('email',)                             # Default ordering

# Register the custom user model and admin class
admin.site.register(CustomUser, CustomUserAdmin)
