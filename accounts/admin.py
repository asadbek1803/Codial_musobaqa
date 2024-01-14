from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import Account


# Register your models here.
@admin.register(Account)
class AccountAdmin(UserAdmin):
    list_display = ('id', 'first_name', 'last_name', 'username', 'email', 'phone_number','soha', 'date_joined', 'is_active')
    readonly_fields = ('date_joined', 'last_login')
    search_fields = ('id', 'first_name', 'last_name', 'username', 'email')
    ordering = ('-date_joined', )
    list_display_links = ('id', 'first_name', 'last_name')
    # Neeed else returned error
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()