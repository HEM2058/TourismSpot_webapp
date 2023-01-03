from django.db import models

# Create your models here.

class Contributor(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    phone = models.BigIntegerField()
    otp = models.IntegerField()
    bio = models.CharField(max_length=250)
    lat = models.FloatField()
    lng = models.FloatField()
    is_active = models.BooleanField(default=True)
    Date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(null=True)

    def __str__(self):
        return self.fname
    