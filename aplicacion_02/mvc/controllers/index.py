import web
from mvc.models.modelo_index import ModeloIndex

render = web.template.render('mvc/views/', base='layout')

m_index = ModeloIndex()

class Index:
    def GET(self):
        try:
            resultado = m_index.consultaProductos()
            return render.index(datos=resultado)  # Pasa los datos como un diccionario
        except Exception as e:
            print(f"Error 101 - index {e.args}")
            return "Ups, algo salió mal"