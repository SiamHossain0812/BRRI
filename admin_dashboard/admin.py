from django.contrib import admin
from .models import UserInfo

@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'address', 'user_id', 'password', 'gateway_id')
    search_fields = ('name', 'phone', 'user_id', 'gateway_id')
    list_filter = ('gateway_id',)


from django.contrib import admin
from .models import AdminInfo

class AdminInfoAdmin(admin.ModelAdmin):
    # If you want to control the fields that can be seen/edited in the Admin Panel
    list_display = ['name', 'phone', 'address', 'user_id']  # Fields to display in the list view
    
    # To restrict adding new AdminInfo records only to superusers
    def has_add_permission(self, request):
        # Only allow superusers to add new records
        return request.user.is_superuser

    # Optional: Restrict deleting/editing of AdminInfo records to superusers
    def has_change_permission(self, request, obj=None):
        # Only allow superusers to change records
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        # Only allow superusers to delete records
        return request.user.is_superuser
    
    # Optional: If you want to filter the data to show only admin records for superusers
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset  # Superusers can see all records
        return queryset.none()  # Non-superusers won't see any records

# Register the AdminInfo model with the custom admin
admin.site.register(AdminInfo, AdminInfoAdmin)
