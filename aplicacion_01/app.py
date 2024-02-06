import web

urls = (
     '/',"hello",
     "/pagina2","pagina2"
)
app = web.application(urls, globals())

class hello:
    def GET(self):
        return "ahhhhh"
    
class pagina2:
    def GET(self):
        return "hola pagina 2"

if __name__ == "__main__":
    app.run()