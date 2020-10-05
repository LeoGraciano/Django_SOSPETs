from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Pet(models.Model):
    cidade = models.CharField(max_length=50)
    descrição = models.TextField()
    telefone = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
    data_de_crianção = models.DateTimeField(auto_now_add=True)
    foto = models.ImageField(upload_to='pet')
    ativo = models.BooleanField(default=True)
    usuário = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'pet'
        pass
