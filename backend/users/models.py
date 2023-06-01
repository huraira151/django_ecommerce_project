from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
from users.managers import UserManager
from django.utils.translation import gettext_lazy as _

Customer = "customer"
Seller = "seller"

ROLE_CHOICE = (
    (Customer, 'Customer'),
    (Seller, 'Seller'),
)


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(null=True, blank=True, max_length=255)
    email = models.EmailField(null=True, blank=True, max_length=255, unique=True)
    image = models.ImageField(upload_to="user", null=True, blank=True)
    timestamp_created = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    last_updated = models.DateTimeField(null=True, blank=True, auto_now=True)
    role = models.CharField(default=Customer, choices=ROLE_CHOICE, max_length=20)
    phone_number = PhoneNumberField(null=True, blank=True)
    stripe_customer_id = models.CharField(max_length=100, null=True, blank=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return self.is_staff


class Seller(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='seller_user')
    profile_pic = models.FileField(upload_to='seller', null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = PhoneNumberField()
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name
