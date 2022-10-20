from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publishment = models.CharField(max_length=255, blank=True)
    translator = models.CharField(max_length=255, blank=True)
    publish_year = models.PositiveIntegerField(validators=[MinValueValidator(1800), MaxValueValidator(2020)])