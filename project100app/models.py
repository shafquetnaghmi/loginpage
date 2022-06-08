from django.db import models
from django.contrib.auth.models import User


class user_type(models.Model):
    select_choices=(
        ('doctor','doctor'),('patient','patient')
    )
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    is_doctor=models.BooleanField(default=False)
    is_patient=models.BooleanField(default=False)
    photo=models.ImageField(default='default.jpg',upload_to='profile_pic')
    adress=models.TextField(max_length=200)
    #doctor_or_patient=models.CharField(max_length=200,choices=select_choices)
    def __str__(self):
        return self.user.username

    

