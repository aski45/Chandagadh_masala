from django.db import models

# Create your models here.


class Product(models.Model) :

    name        =   models.TextField(max_length = 200)
  
    price       =   models.IntegerField(null = False)

    # offer       =   models.TextField(blank = True)

    discription   = models.TextField(max_length = 300)

    image        = models.ImageField(upload_to='products',default='products/default.jpg') 

    def __str__(self):
        return self.name



class Member(models.Model):

    name            =   models.TextField(max_length = 200)

    designation    =   models.TextField(max_length = 200)

    discription   = models.TextField(max_length = 300)

    profile        = models.ImageField(upload_to='profile', default='profile/default.jpg')

    def __str__(self):
        return self.name