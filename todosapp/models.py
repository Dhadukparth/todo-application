from django.db import models

# Create your models here.

class todos(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    description = models.TextField(default="")

    def __str__(self):
        return self.name

    class meta:
        db_table = "Todos"

    
