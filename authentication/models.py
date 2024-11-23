from django.db import models

# Create your models here.

class User(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=100)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    password = models.CharField(max_length=255)
    registration_date = models.DateTimeField(auto_now_add=True)
    user_level = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'