from typing import Any
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class UserManager(BaseUserManager):
    def create_user(self, email, username, name, is_admin=False, password=None):
        """
        Creates and saves a User with the given email, username, name and password.
        """
        if not email:
            raise ValueError("User must have an email address")
        if not username:
            raise ValueError("Users must have a username")
        
        user = self.model(
            email=self.normalize_email(email),
            username=username,  
            name=name,  
            is_admin=is_admin
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, name, is_admin=True, password=None):
        """
        Creates and saves a Superuser with the given email, username, name and password.
        """
        user = self.create_user(
            email=email,
            username=username,  
            name=name,  
            password=password,
            is_admin=is_admin
        ) 
        user.is_admin = True
        user.save(using=self._db)
        return user
    
class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="Email",
        max_length=250,
        unique=True,
    )
    username = models.CharField(max_length=150, unique=True)  
    name = models.CharField(max_length=250)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True) 
    is_superuser = models.BooleanField(default=False)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ["email", "name"]  

    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True

class Workout(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    target_muscles = models.CharField(max_length=250)

    def __str__(self):
        return self.name
    
class WorkoutPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workouts = models.ManyToManyField(Workout)
    goal = models.CharField(max_length=300)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.user.username}'s Plan {self.goal}"
    
class NutritionPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meals_per_day = models.IntegerField()
    calories_per_day = models.FloatField()

    def __str__(self):
        return f"{self.user.username} - {self.calories_per_day}"
    
class WorkoutProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    notes = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.date}"
