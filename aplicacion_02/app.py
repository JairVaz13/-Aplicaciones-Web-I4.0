import web

# Definir las URLs y el objeto de renderizado
urls = (
    "/", "mvc.controllers.index.Index",
    "/contactos", "mvc.controllers.contactos.Contactos",
    "/productos", "mvc.controllers.productos.Productos"
)

render = web.template.render('mvc/views/')

# Crear la aplicación web
app = web.application(urls, globals())

# Definir la clase para la gestión de productos
class Productos:
    def GET(self):
        return render.productos()

if __name__ == "__main__":
    # Configurar la aplicación para no estar en modo de depuración
    web.config.debug = True

    # Ejecutar la aplicación web
    app.run()