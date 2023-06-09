from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
from users.managers import UserManager
from django.utils.translation import gettext_lazy as _

# Imports for Forgot Password
from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.conf import settings


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

    def get_username(self):
        return self.email

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name


class Seller(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='seller_user')
    profile_pic = models.FileField(upload_to='seller', null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = PhoneNumberField()
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name


# Forgot Password Signal to send email
@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    """
    Handles password reset tokens
    When a token is created, an e-mail needs to be sent to the user
    :param sender: View Class that sent the signal
    :param instance: View Instance that sent the signal
    :param reset_password_token: Token Model Object
    :param args:
    :param kwargs:
    :return:
    """
    # send an e-mail to the user
    context = {
        'name': reset_password_token.user.name,
        'reset_password_token': reset_password_token.key
    }

    # render email text
    email_html_message = render_to_string('email/user_reset_password.html', context)
    email_plaintext_message = render_to_string('email/user_reset_password.txt', context)

    msg = EmailMultiAlternatives(
        # title:
        "Password Reset for {title}".format(title="Ecommerce Project"),
        # message:
        email_plaintext_message,
        # from:
        settings.EMAIL_HOST_USER,
        # to:
        [reset_password_token.user.email]
    )
    msg.attach_alternative(email_html_message, "text/html")
    msg.send()
