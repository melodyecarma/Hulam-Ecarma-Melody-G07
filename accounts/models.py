from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        STUDENT = "STUDENT", "Student"
        ADMIN = "ADMIN", "Administrator"

    email = models.EmailField("email address", unique=True)

    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.STUDENT,
    )
    department = models.CharField("school / department", max_length=100, blank=True)
    contact_number = models.CharField(
        max_length=20,
        blank=True,
        validators=[RegexValidator(
            r"^[0-9+\-\s()]{7,20}$",
            "Enter a valid contact number (digits, spaces, +, -, parentheses).",
        )],
    )
    profile_photo = models.ImageField(upload_to="profile_photos/", blank=True, null=True)

    def save(self, *args, **kwargs):
        # Superusers are always Administrators
        if self.is_superuser:
            self.role = self.Role.ADMIN
        super().save(*args, **kwargs)