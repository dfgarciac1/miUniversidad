from django.db import models

# Create your models here.
class Carrera(models.Model):
    codigo= models.CharField(max_length=3,primary_key=True)
    nombre = models.CharField(max_length=50)
    duracion = models.positiveSmallIntegerField(default=5)

class Estudiante(models.Model):
    dni= models.CharField(max_length=8,primary_key=True)
    apellidoPaterno=models.charField(max_length=35)
    apellidoMaterno=models.charField(max_length=35)
    nombres = models.CharField(max_length=35)
    fechaNacimiento=models.DateField()
    sexos = [ 
        ('F','Femenino'),
        ('M','Masculino')]
     sexo = models.CharField(max_length=1,choices=sexos,default='F')
     carrera= models.foreingKey(Carrera,null=False,blank=False,on_delate=models.CASCADE)
     vigencia= models.BooleanField(default=True)

     def nombreCompleto(self):
         texto="{0},{1},{2}"
         return texto.Format(self.apellidoPaterno,self.apellidoMaterno,self.nombres)

    class Curso(models.Model):
        codigo = models.CharField(max_length=6,primary_key=True)
        nombre = models.CharField(max_length=30)
        creditos=models.PositiveSmallIntegerField()
        docente= models.CharField(max_length=100)

    class Matricula(models.Model):
        id=models.AutoField(primary_key=True)
        estudiante=models.ForeignKey(Estudiante,null=False,blank=False,on_delate=models.CASCADE)
        fechaMatricula=models.DataTimeField(auto_now_add=True)