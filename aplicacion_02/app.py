"""framework web.py"""
import web
# rutasde los contraladores
urls = (
    '/', 'mvc.controllers.hello.Hello'
    ,"/pagina2","mvc.controllers.hello.Pagina2."    
)
app = web.application(urls, globals())


    
# punto de entrada 
if __name__ == "__main__":
    app.run()