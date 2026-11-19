import os
from django.db import models
from django.utils.timezone import now
from django.conf import settings
# Create your models here.

def upload_to_app_static(instance, filename):
    # This points directly to: your_project/your_app_name/static/images/
    # Adjust 'your_app_name' to match your actual app folder name    
    return os.path.join(settings.BASE_DIR, 'Ecommerceapp', 'static', '', filename)

class Users(models.Model):
        name = models.CharField(max_length=50)
        age = models.IntegerField()
        emailID = models.CharField(max_length=50)
        phone = models.IntegerField(10)
        adminuser = models.CharField()
        dateofjoin = models.DateTimeField(default=now)
        updatedate = models.DateTimeField(default=now)
        username = models.CharField(25)
        password = models.CharField(400)
        userphoto = models.ImageField()
        genter = models.CharField(max_length=6)

        def __str__(self):
                return ("Name: {0} and {1}".format(self.name,self.username))

class Address(models.Model):
        user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
        address = models.CharField(max_length=200)
        city = models.CharField(max_length=20)
        state = models.CharField(max_length=20)
        pincode = models.CharField(max_length=6)
        dateofadd = models.DateTimeField(default=now)
        dateofupdate = models.DateTimeField(default=now)
        
        def __str__(self):
                return ("Name: {0}, {1}, {2}, {3} and {4}".format(self.address,self.city,self.state))

class Producttype(models.Model):
        producttype = models.CharField(max_length=200)
        productimage = models.ImageField()
        dateofadd = models.DateTimeField(default=now)
        dateofupdate = models.DateTimeField(default=now)

        def __str__(self):
                return ("Name: {0} and {1}".format(self.producttype,self.productimage))

class Productdetails(models.Model):
        productid = models.ForeignKey(Producttype, on_delete=models.CASCADE)
        itemname = models.CharField(max_length=300)     
        itemimage = models.ImageField(upload_to=upload_to_app_static, blank=True, null=True)
        rate = models.IntegerField()
        summary = models.CharField(max_length=500)
        description = models.CharField(max_length=5000)
        dateofadd = models.DateTimeField(default=now)
        dateofupdate = models.DateTimeField(default=now)

        def __str__(self):
                return ("Name: {0}, {1} and {2}".format(self.itemname,self.itemimage,self.rate))

class Productimages(models.Model):
        productid = models.ForeignKey(Productdetails, on_delete=models.CASCADE)
        itemimages = models.ImageField(upload_to=upload_to_app_static, blank=True, null=True)
        dateofadd = models.DateTimeField(default=now)
        dateofupdate = models.DateTimeField(default=now)

        def __str__(self):
                return ("Name: {0}".format(self.itemimages))

class ProductReviews(models.Model):
        productid = models.ForeignKey(Productdetails, on_delete=models.CASCADE)
        userid = models.ForeignKey(Users, on_delete=models.CASCADE)
        reviewcomments = models.CharField(max_length=5000)
        dateofadd = models.DateTimeField(default=now)   
        dateofupdate = models.DateTimeField(default=now)
        def __str__(self):
                return ("Name: {0}".format(self.reviewcomments))      


class Orderconfirm(models.Model):
        userid = models.ForeignKey(Users, on_delete=models.CASCADE)
        totalamount = models.IntegerField()        
        paymentstatus = models.CharField(max_length=10)
        paymentmode = models.CharField(max_length=10)
        orderconfirm = models.CharField(max_length=20)
        dateofconfirm = models.DateTimeField(default=now)

        
class Orderdetails(models.Model):
        orderconfirmid = models.ForeignKey(Orderconfirm, on_delete=models.CASCADE)
        itemid = models.ForeignKey(Productdetails, on_delete=models.CASCADE)
        quantity = models.IntegerField()
        amount = models.IntegerField()

class Deliverydetails(models.Model):
        orderconfirmid = models.ForeignKey(Orderconfirm, on_delete=models.CASCADE)
        deliverystatus = models.CharField(max_length=20)
        dateofdelivery = models.DateTimeField(default=now)

class Cartitems(models.Model):        
        itemid = models.ForeignKey(Productdetails, on_delete=models.CASCADE)
        quantity = models.IntegerField()
        userid = models.ForeignKey(Users, on_delete=models.CASCADE)
        dateodadd = models.DateTimeField(default=now)
        
