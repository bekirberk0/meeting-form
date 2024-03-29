from django.db import models

# Create your models here.
class Meetings(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    