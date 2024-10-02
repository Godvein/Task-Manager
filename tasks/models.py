from django.db import models

# Create your models here.
class Tasks(models.Model):
    name = models.TextField(max_length=50)
    description = models.TextField(max_length=500)
    complete = models.BooleanField(default=False)
    registeredtime = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
