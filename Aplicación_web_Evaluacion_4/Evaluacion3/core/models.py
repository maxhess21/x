from django.db import models    



class categoria_libro(models.Model):
    id_categoria= models.IntegerField(primary_key=True, verbose_name='Id de categoria')
    nombre_categoria = models.CharField(max_length=50,  verbose_name='Nombre de categoria')


    def __str__(self):
        return self.nombre_categoria
  


class Libro(models.Model):
    id_libro = models.IntegerField(primary_key=True ,  verbose_name= 'Id del libro')
    nombre_libro = models.CharField(max_length=50,  verbose_name= 'Nombre del libro')
    autor_libro = models.CharField(max_length=50,  verbose_name= 'Autor del libro')
    descripcion_libro = models.CharField(max_length=50 , verbose_name='Descripcion del libro')
    categoria_libro = models.ForeignKey(categoria_libro, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_libro