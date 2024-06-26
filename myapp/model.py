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

    def __str__(self):
        return self.type


class Employee(models.Model):
    
    name=models.CharField(max_length=500)
    email=models.CharField(max_length=50)
    addres=models.CharField(max_length=200)
    phone=models.CharField(max_length=120)
    about=models.TextField()
    position=models.CharField(max_length=120,choices=
                          (('Manager','manager'),
                           ('Software-developer','sd'),
                           ('project Leader','pl')
                           ))
    company=models.ForeignKey(Company,on_delete=models.CASCADE)

