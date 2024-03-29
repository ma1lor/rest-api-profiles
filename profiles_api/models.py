from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profile"""


    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email adress')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)


        return user

    def create_superuser(self, email, name, password):
        """create and save a new superuser with given details"""

        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_stuff = AbstractBaseUser
        user.save(using=self._db)

        return users





class UserProfile(AbstractBaseUser, PermissionsMixin):
    """

    Database model for users in system

    """

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_activate = models.BooleanField(default=True)
    is_stuff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'name'
    ]
    def get_full_name(self):
        """
        Retrieve full name of User

        """
        return self.name
    def get_short_name(self):

        """
        Retrieve short name of User
        """

        return self.name


    def __str__(self):
        """Return string representation of our user"""
        return self.email

# Create your models here.
