from django.db import models
from accounts.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import datetime
from django.core.exceptions import ValidationError



# Create your models here.

def birth_date_validation(value):
    current_year = datetime.datetime.now().year
    if value < 1950 or value > current_year:
        raise ValidationError(
            'Year of birth must be after 1950 and cannot be in the future.'
        )

SPECIES = (
    ('Cat', 'CAT'),
    ('Dog', 'DOG'),
    ('Hamster', 'HAMSTER')
)

class Pet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    species = models.CharField(choices=SPECIES, max_length=10, default='cat')
    year_of_birth = models.PositiveSmallIntegerField(
        validators=[birth_date_validation]
    )


    def __str__(self):
        return self.species

    class Meta:
        verbose_name_plural = "Pets"




