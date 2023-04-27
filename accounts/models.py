from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserAccountManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('Users must have an email addresss')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email


class UserProfile(models.Model):
    user = models.OneToOneField(
        UserAccount,
        on_delete=models.CASCADE,
        related_name='profile',
    )
    phone = models.CharField(
        max_length=11
    )
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        new_arr = []
        for i in str(self.user):
            if i == '@':
                break
            new_arr.append(i)
        self.slug = ''.join(new_arr)
        super(UserProfile, self).save(*args, **kwargs)
