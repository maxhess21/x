from rest_framework import serializers
from core.models import Libro ,categoria_libro



class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = ['id_libro','nombre_libro','autor_libro','descripcion_libro','categoria_libro']