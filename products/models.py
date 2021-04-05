import random
import os
from django.db import models

def get_filename_ext(filename):
    base_name = os.path.basename(filename)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    print(instance)
    print(filename)
    name, ext = get_filename_ext(filename)
    new_filename = random.randint(1, 23849283098)
    final_filename = f'{new_filename}.{ext}'

    return f'products/{new_filename}/{final_filename}'


class Product(models.Model):
    title         = models.CharField(max_length=120)
    description   = models.TextField()
    price         = models.DecimalField(decimal_places=2, max_digits=20, default=39.99)
    '''
        * blank=True means this field is not required
    '''
    image         = models.ImageField(upload_to=upload_image_path, null=True, blank=True)


    def __str__(self):
        return self.title
