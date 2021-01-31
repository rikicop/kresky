from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    def __str__(self):
        template = '{0.name} {0.email} {0.subject} {0.message}'
        return template.format(self)  
