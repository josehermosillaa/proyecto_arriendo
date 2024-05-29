from .models import Inmueble, Tipo_inmueble, User

def get_all_inmubles():
    pass

def insertar_inmuble():
    pass
def actualizar_inmueble():
    pass
def borrar_inmueble():
    pass


def get_list_inmuebles(comuna):
    select = f"""
    SELECT A.id,C.comuna, B.region, nombre_inmueble,direccion  FROM app_inmueble as A
    INNER JOIN app_region as B
	ON A.id_region_id = B.id
    INNER JOIN app_comuna as C
	ON A.id_comuna_id = C.id
    WHERE C.comuna like '{comuna}'
    """

    query = Inmueble.objects.raw(select)

    #crear el archivo con la salida
    for p in query:
        print(p.nombre_inmueble)
        print(p.comuna)
        print(p.region)
        print(p.direccion)

def get_inmuebles(region):
    select = f"""
    SELECT A.id,C.comuna, B.region, nombre_inmueble,direccion  FROM app_inmueble as A
    INNER JOIN app_region as B
	ON A.id_region_id = B.id
    INNER JOIN app_comuna as C
	ON A.id_comuna_id = C.id
    WHERE C.comuna like '{region}'
    """

    query = Inmueble.objects.raw(select)

    #crear el archivo con la salida
    for p in query:
        print(p.nombre_inmueble)
        print(p.comuna)
        print(p.region)
        print(p.direccion)