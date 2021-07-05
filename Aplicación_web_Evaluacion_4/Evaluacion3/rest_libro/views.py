from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Libro
from rest_libro.serializers import LibroSerializer


@csrf_exempt
@api_view(['GET', 'POST'])
def lista_libros(request):
    """
    lista de libros
    """
    if request.method == 'GET':
        Libros = Libro.objects.all()
        serializer = LibroSerializer(Libros, many=True) 
        return Response(serializer.data)

    elif request.method == 'POST':
        data= JSONParser().parse(request)
        serializer = LibroSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET','PUT','DETELE'])
def detalle_libro(request, id):
    """
    Retrieve, update or delete a code Libro.
    """
    try:
        Libros = Libro.objects.get(id_libro=id)
    except Libro.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = LibroSerializer(Libros)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = LibroSerializer(Libros, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        Libros.delete()
        return HttpResponse(status=204)


