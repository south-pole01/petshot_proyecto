from django.db import models

# Create your models here.
ANIMALES = (
    ('Perros', 'Perros'),
    ('Gatos', 'Gatos'),
    ('Aves', 'Aves'),
    ('Roedores', 'Roedores'),
    ('Otros', 'Otros')
)

class Adopta (models.Model):
    fotografia = models.ImageField(upload_to='adopciones')
    nombreMascota = models.CharField(max_length=20)
    edad = models.IntegerField()
    ciudad = models.CharField(max_length=50)
    email = models.EmailField(max_length=70,unique= True)
    tipo_animal = models.CharField(max_length=50, choices=ANIMALES)

    def __str__(self):
        return str(self.fotografia)
