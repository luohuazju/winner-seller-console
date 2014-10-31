from django.db import models

# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=128)
    create_date = models.DateTimeField('Create Date')
    update_date = models.DateTimeField('Update Date')

class User(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    create_date = models.DateTimeField('Create Date')
    update_date = models.DateTimeField('Update Date')
    roles = models.ManyToManyField(Role)

