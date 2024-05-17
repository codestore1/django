from django.db import models

# Create your models here.

class Company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=500)
    location=models.CharField(max_length=500)
    about=models.TextField()
    type=models.CharField(max_length=100,choices=
                          (('IT','IT'),
                           ('Non-IT','Non-IT'),
                           ('mobile phones','Others')
                           ))
    added_data=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=False)

