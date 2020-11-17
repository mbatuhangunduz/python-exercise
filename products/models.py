from django.db import models
from django.urls import reverse


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)  # max_length
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=1000)
    summary = models.TextField(blank=False, null=True)
    featured = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={"id": self.id})  # f"/products/{self.id}" (reverse komutu ile url adı değişse bile linke tıklandığında ilgili adrese gidiş sağlanır.)
