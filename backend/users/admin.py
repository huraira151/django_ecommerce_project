from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from .forms import UserChangeForm, UserCreationForm
from .models import Seller

User = get_user_model()


@admin.register(User)
class CustomUserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (("User", {"fields": ("email", "name", "phone_number", "stripe_customer_id", "image", "is_staff",
                                      "is_superuser", "is_active", "password")}),)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'role', 'password1', 'password2'),
        }),
    )
    list_display = ["id", 'email', "name", 'role', "is_active"]
    search_fields = ["name", "email", "role"]
    ordering = ['email']


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
