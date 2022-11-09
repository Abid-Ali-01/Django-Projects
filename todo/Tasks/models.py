from django.db import models

# Create your models here.


class Tasks(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    Created = models.DateTimeField(auto_now_add=True)

 
def __self__(self):
    return self.title
