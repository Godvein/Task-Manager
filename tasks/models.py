from django.db import models

# Create your models here.
class Tasks(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=50)
    description = models.TextField(max_length=500)
    registeredtime = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name