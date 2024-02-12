import web
import json  
from mvc.models.index import ModeloIndex

render = web.template.render('mvc/views/')
m_index = ModeloIndex()

class Index:
    def GET(self):
        try:
            contactos_json = m_index.obtener_contactos_json()
            contactos = json.loads(contactos_json)
            return render.index(contactos=contactos)
        except Exception as e:
            print(f"Error: {e}")
            return "Lo siento, algo salió mal."


class Productos:
    def GET(self):
        try:
            return render.productos()
        except Exception as e:
            return "Lo siento algo salio mal"
            print (f"Error 101 - index {e.args}")

class Contactos:
    def GET(self):
        try:
            return render.contactos()
        except Exception as e:
            return "Lo siento algo salio mal"
            print (f"Error 101 - index {e.args}")