from django.db import models

# Create your models here.
class user_details(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=1000)
    email = models.EmailField(max_length=250,primary_key=True)
    address = models.TextField()
    zip_code = models.CharField(max_length=8)
class products(models.Model):
    id = models.CharField(max_length=100,primary_key=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    desc = models.TextField()
    main = models.ImageField(upload_to='pics')
    im1 = models.ImageField(upload_to='pics')
    im2 = models.ImageField(upload_to='pics')
    im3 = models.ImageField(upload_to='pics')
    im4 = models.ImageField(upload_to='pics')
    stock = models.IntegerField()
    category = models.CharField(max_length=50,default='shoe')
class user_products(models.Model):
    id = models.IntegerField(primary_key=True)
    email = models.EmailField(max_length=250)
    pro_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
   
    

    
    
