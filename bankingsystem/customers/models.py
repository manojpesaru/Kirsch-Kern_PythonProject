from django.db import models

# Create your models here.

class Customer(models.Model):
    firstName = models.CharField(max_length=60)
    lastName = models.CharField(max_length=60)
    dob = models.DateField()


    def __str__(self):
        return self.lastName

class CustomerAddress(models.Model):
    user = models.OneToOneField(
        Customer,
        related_name='address',
        on_delete=models.CASCADE,
    )
    street_address = models.CharField(max_length=512)
    city = models.CharField(max_length=256)
    postal_code = models.PositiveSmallIntegerField()
    country = models.CharField(max_length=256)

    def __str__(self):
        return self.user.firstName+self.user.lastName