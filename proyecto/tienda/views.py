from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Producto


@api_view(['GET'])
def listar_productos(request):
    productos = Producto.objects.all().values()
    return Response({"productos": list(productos)})
