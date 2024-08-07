from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class UserProfileM(BaseUserManager):
    def create_user(self, email, cc, name, age, gender, phone, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        if not cc:
            raise ValueError('The CC field must be set')
        
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            cc=cc,
            name=name,
            age=age,
            gender=gender,
            phone=phone,
            **extra_fields
        )
        user.save(using=self._db)
        return user

    def create_superuser(self, email, cc, name, age, gender, phone, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(
            email=email,
            cc=cc,
            name=name,
            age=age,
            gender=gender,
            phone=phone,
            **extra_fields
        )

class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    cc = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileM()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['cc', 'name', 'age', 'gender', 'phone']

    def check_password(self, raw_password):
        
        return self.cc == raw_password

    def set_password(self, raw_password):
        
        pass

    def __str__(self):
        return self.email
