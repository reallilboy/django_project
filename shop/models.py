from django.db import models
import datetime
# Create your models here.



class Category(models.Model):
        name = models.CharField(max_length=50)


        def __str__(self):
                return self.name


        

class Customer(models.Model):
        f_name = models.CharField(max_length=50)
        l_name = models.CharField(max_length=50)
        phone = models.CharField(max_length=50)
        email = models.EmailField(max_length=40)
        password = models.CharField(max_length=20)

class Product(models.Model):
        name = models.CharField(max_length=60)
        price = models.DecimalField(max_digits=50,default=0,decimal_places=2)
        category = models.ForeignKey(Category,on_delete=models.CASCADE, default=1)
        desc = models.CharField(max_length=200,default='',blank=True,null=True)
        image = models.ImageField(upload_to='uploads/product')

        def __str__(self):
                return self.name

class Order(models.Model):
        product = models.ForeignKey(Product,on_delete=models.CASCADE)
        customer = models.ForeignKey(Category,on_delete=models.CASCADE)
        quantity = models.IntegerField(default=1)
        address = models.CharField(max_length=40)
        phone = models.CharField(max_length=30)
        date = models.DateField(default=datetime.datetime.today)
        status = models.BooleanField(default=False)

        def __str__(self):
                return self.product
