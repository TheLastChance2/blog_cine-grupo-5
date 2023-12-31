from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categorias(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.nombre


class Post(models.Model):
    titulo = models.CharField(max_length=255)
    cuerpo = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(default='static/img/Logo.png')
    categoria_post = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete= models.CASCADE, default = 0)
    
    def comentarios_realizados(self):
        return self.comentario_set.all()

    def __str__(self) -> str:
        return self.titulo
    
class Comentario(models.Model):
    texto = models.TextField(max_length= 1000)
    fecha_comentacion = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    usuario = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self) -> str:
        return f"{self.post} {self.texto}"
    
opciones_consultas = [
    [0, "consulta"],
    [1, "reclamo"],
    [2, "sugerencia"],
    [3, "felicitaciones"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length = 50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre