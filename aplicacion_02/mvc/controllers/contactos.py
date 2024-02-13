import web

render = web.template.render('mvc/views/')

class Contactos:
    def GET(self):
        return render.contactos()