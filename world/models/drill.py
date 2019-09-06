from pydrill.client import PyDrill




def simplequery(shape_id):
    drill = PyDrill(host='localhost', port='8047')
    drill.storage_enable('mongo')
    shapes = drill.query('SELECT * FROM mongo.geoms.collection where 1=0')
    for shape in shapes:
        print(shape)

