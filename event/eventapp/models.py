from django.db import models
# from django.contrib.auth.models import AbstractUser


# class User(AbstractUser):
#     usertype = models.CharField(max_length=50)

class Event(models.Model):
    img=models.ImageField(upload_to="pic")
    name=models.CharField(max_length=50)
    desc=models.CharField(max_length=50)
    def __str__(self):
        return self.name 
        


class Booking(models.Model):
    cus_name=models.CharField(max_length=55)
    cus_ph=models.CharField(max_length=12)
    name=models.ForeignKey(Event,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booked_on=models.DateField(auto_now=True)    

































# class Customer(models.Model):
#     customer_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     address = models.CharField(max_length=50)
#     phone = models.IntegerField()
#     email = models.EmailField()


# class Event(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     date = models.DateField()
#     location = models.CharField(max_length=100)
    

# class Enquiry(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     event = models.ForeignKey(Event, on_delete=models.CASCADE)
#     enquiry_date = models.DateField()
#     details = models.TextField()

# class Package(models.Model):
#     name = models.CharField(max_length=100)
#     details = models.TextField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)


# class Booking(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     event = models.ForeignKey(Event, on_delete=models.CASCADE)
#     package = models.ForeignKey(Package, on_delete=models.CASCADE)
#     booking_date = models.DateField()
