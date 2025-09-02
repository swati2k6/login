from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    fieldsets = DjangoUserAdmin.fieldsets + (
        ('Role & Profile', {'fields': ('role', 'profile_picture')}),
        ('Address', {'fields': ('address_line1', 'city', 'state', 'pincode')}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'role')

