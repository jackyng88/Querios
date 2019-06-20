from django_registration.forms import RegistrationForm
from users.models import CustomUser


class CustomUserForm(RegistrationForm):
    # Class for custom user form extending from Django's registration form

    class Meta(RegistrationForm.Meta):
        model = CustomUser