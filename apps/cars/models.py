from django.db import models

class CarModel(models.Model):
    model_no=models.CharField(max_length=4)
    name=models.CharField(max_length=20)
    descripe=models.TextField(max_length=50)
    create_at=models.DateTimeField(auto_now_add=True)
    updated_to=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.model_no}"

