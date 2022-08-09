from ast import mod
import profile
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, username, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, username, password, **other_fields)

    def create_user(self, email, username, password=None, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, username=username,**other_fields)
        user.set_password(password)
        user.save()
        return user


class NewUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(_(
        'about'), max_length=500, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username


class Userprofile(models.Model):

    user = models.OneToOneField(NewUser,on_delete=models.CASCADE)
    last_name = models.CharField(max_length=225,blank=True)
    date_of_birth = models.DateField()
    profile_photo = models.ImageField(upload_to='media/images/user') 
    cv = models.FileField(upload_to='media/cv/user')
    about = models.TextField()


    def __str__(self) :

        return self.user.first_name

class Education(models.Model):

    profile = models.ForeignKey(NewUser,on_delete=models.CASCADE)
    university = models.CharField(max_length=225,null=True)
    department = models.CharField(max_length=250,null=True)
    remark = models.CharField(max_length=225,null=True)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):

        return self.profile.email
class Experience(models.Model):
    profile = models.ForeignKey(NewUser,on_delete=models.CASCADE)
    company = models.CharField(max_length=225,null=True)
    position = models.CharField(max_length=250,null=True)
    remark_e = models.CharField(max_length=225,null=True)
    start_date_e = models.DateField()
    end_date_e = models.DateField()
    def __str__(self):

        return self.profile.email




