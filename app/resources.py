from import_export import resources
#from .models import *
from app.models import *


class ProduccionResource(resources.ModelResource):
    class Meta:
        model = Produccion



class AlmacenResource(resources.ModelResource):
    class Meta:
        model = Almacen