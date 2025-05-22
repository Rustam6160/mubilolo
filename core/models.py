from django.db import models

# Create your models here.
from django.db import models

class Gift(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    for_whom = models.CharField(max_length=100)
    link = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
