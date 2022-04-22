from django.db import models

# Create your models here.

class Todolist(models.Model):
    text = models.CharField(max_length=45)
    completed = models.BooleanField(default=False)

# Function to return text as a representation of todolist, self is used to return whatever we write in text that would be returned as string.
    def __str__(self):
        return self.text
