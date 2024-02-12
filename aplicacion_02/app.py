import web

urls = (
    '/', 'mvc.controllers.hello.Index', 
    '/productos', 'mvc.controllers.hello.Productos',
    '/contactos', 'mvc.controllers.hello.Contactos'
)
app = web.application(urls, globals())


if _name_ == "_main_":
    web.config.debug= False
    app.run()