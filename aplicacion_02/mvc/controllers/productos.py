import web

render = web.template.render('mvc/views/')

class Productos:
    def GET(self):
        try:  
            return render.productos()
        exepct Exception as e:
            return "Error " + str(e.args) + str(e.message)