from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='followed_by', blank=True)

    # Set custom related_name for the conflicting fields
    groups = models.ManyToManyField(
        'auth.Group', 
        related_name='customuser_set', 
        blank=True,
        help_text="The groups this user belongs to."
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission', 
        related_name='customuser_set', 
        blank=True,
        help_text="Specific permissions for this user."
    )

    def __str__(self):
        return self.username
