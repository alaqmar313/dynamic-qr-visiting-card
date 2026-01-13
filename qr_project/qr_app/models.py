from django.db import models

# Create your models here.
class VisitingCard(models.Model):
    uid = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    company = models.CharField(max_length=100, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.name