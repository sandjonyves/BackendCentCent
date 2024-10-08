from typing import Any, Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin, AbstractBaseUser
from django.utils import timezone
from store.models import Restaurant
class CustomUserManager(BaseUserManager):
    def _create_user(self, matricule_or_email, password=None, **extra_fields):
        if not matricule_or_email:
            raise ValueError('Le matricule ou l\'email doit être spécifié.')
        
        if '@' in matricule_or_email:  # Assuming it's an email
            user = self.model(email=matricule_or_email, **extra_fields)
        else:  # It's a matricule
            user = self.model(matricule=matricule_or_email, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_user(self, matricule, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('role', CustomUser.Role.ETUDIANT)
        return self._create_user(matricule, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', CustomUser.Role.ADMIN)
        return self._create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, blank=True, null=True)
    matricule = models.CharField(max_length=32, unique=True, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'matricule' # Pour les étudiants et les marchands
    REQUIRED_FIELDS = ['username']  # Peut être vide pour les admins

    class Role(models.TextChoices):
        ETUDIANT = "ETUDIANT", "étudiant"
        MARCHAND = "MARCHAND", "marchand"
        ADMIN = "ADMIN", "admin"

    role = models.CharField(max_length=32, choices=Role.choices, default="")
class EtudiantManager(models.Manager):
  def get_queryset(self,*arg,**kwargs) -> models.QuerySet:
    return super().get_queryset(*arg,**kwargs).filter(role=CustomUser.Role.ETUDIANT)

class Etudiant(CustomUser):
  objects = EtudiantManager()
  class Meta:
    proxy = True

  def save(self,*args,**kwargs) -> None:
      if not self.pk:
        self.role = CustomUser.Role.ETUDIANT
        return super().save(*args,**kwargs)

class MarchandManager(models.Manager):
  def get_queryset(self,*arg,**kwargs) -> models.QuerySet:
    return super().get_queryset(*arg,**kwargs).filter(role=CustomUser.Role.MARCHAND)
  #table des marchands
class Marchand(CustomUser):
  objects = MarchandManager()

  class Meta:
    proxy = True

  def save(self,*args,**kwargs) -> None:
    if not self.pk:
      self.role = CustomUser.Role.MARCHAND
      return super().save(*args,**kwargs)

#class de management pour filtre les admins
class AdminManager(models.Manager):
  def get_queryset(self,*arg,**kwargs) -> models.QuerySet:
    return super().get_queryset(*arg,**kwargs).filter(role=CustomUser.Role.ADMIN)

#table des administarteurs
class Admin(CustomUser):
  restaurant_id = models.ForeignKey(Restaurant,on_delete=models.CASCADE,null=True)
  objects = AdminManager()
  # class Meta:
  #   proxy = True

  def save(self,*args,**kwargs) -> None:
    if not self.pk:
      self.role = CustomUser.Role.ADMIN
      return super().save(*args,**kwargs)