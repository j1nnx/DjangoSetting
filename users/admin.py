from django.contrib import admin

from users.models import CustomerUser


@admin.register(CustomerUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "email")
