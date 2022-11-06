
from django.core.validators import MaxValueValidator,MinValueValidator, MaxLengthValidator
from django.db import models



class Thing(models.Model):
    name= models.CharField(max_length=30, unique=True, blank=False)
    description= models.TextField(blank=True, validators= [MaxLengthValidator(120)])
    quantity= models.IntegerField( 
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0),
        ]
    )