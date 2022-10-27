from django.db import models


class Brand(models.Model):
    Name = models.CharField(max_length=255)
    year = models.DateField()
    property = models.IntegerField()
    nationality = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.Name



class Car(models.Model):
    Name = models.CharField(max_length=255)
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE)
    year = models.DateField()
    color = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.Name
