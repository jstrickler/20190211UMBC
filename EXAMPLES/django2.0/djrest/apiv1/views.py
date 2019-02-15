from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
)
import logging

logger = logging.getLogger('django')
local_logger = logging.getLogger('local')
console_logger = logging.getLogger('console')

from superheroes.models import Superhero, Enemy, Power, City

from .serializers import (
    SuperheroSerializer, PowerSerializer, EnemySerializer, CitySerializer
)

# hero endpoints
@api_view(['GET', 'POST'])
def superhero(request):
    logger.info('MESSAGE MESSAGE MESSAGE')
    local_logger.debug("Local message")
    console_logger.debug("You should see this!")
    if request.method == 'GET':
        heroes = Superhero.objects.all()
        serialized = SuperheroSerializer(heroes, many=True)
        return Response(serialized.data)
    else:  # POST
        hero_serializer = SuperheroSerializer(data=request.data)
        if hero_serializer.is_valid():
            hero_serializer.save()
            return Response(hero_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(hero_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def superhero_detail(request, pk):
    if request.method == 'GET':
        hero_obj = Superhero.objects.get(pk=pk)
        serialized = SuperheroSerializer(hero_obj)

        return Response(serialized.data)
    elif request.method == 'POST':
        pass
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass
    elif request.method == 'PATCH':
        pass

# enemy endpoints
class EnemyList(ListAPIView):
    queryset = Enemy.objects.all()
    serializer_class = EnemySerializer

class EnemyDetail(RetrieveAPIView):
    queryset = Enemy.objects.all()
    serializer_class = EnemySerializer

