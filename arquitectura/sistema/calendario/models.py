from django.db import models

# Create your models here.
class Usuario(models.Model):
    rut = models.CharField(primary_key=True, max_length=50)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    
    tipo_de_usuario = (('Paciente','Paciente'),('Medico','Medico'),('Secretaria','Secretaria'))
    tipodeusuario = models.CharField(max_length=40, 
                                       blank=False, null=False, 
                                       verbose_name="tipo de usuario", 
                                       choices=tipo_de_usuario)
    
    
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.rut, self.nombre, self.tipo_de_usuario)