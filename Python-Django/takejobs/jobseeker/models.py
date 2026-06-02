from django.db import models

# Create your models here.
class user(models.Model):
    role_Choice=[("jobseeker","jobseeker"),("company","company")] #key or value ki trakam karta hai
    Email=models.CharField(max_length=30,unique=True)
    password=models.CharField(max_length=15)
    role=models.CharField(max_length=30,choices=role_Choice)
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):# isko hum megic method bolte hai ya dunder method (video number day 4)
        return self.email
class jobseeker(models.Model):
    user_fk=models.ForeignKey(user,on_delete=models.CASCADE)
    f_name=models.CharField(max_length=30)
    l_name=models.CharField(max_length=30)
    number=models.PositiveIntegerField()
    skills=models.CharField(max_length=60)

    def __str__(self):
        return self.f_name+" "+l_name
    