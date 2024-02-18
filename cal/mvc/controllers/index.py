import web
from web import form

render = web.template.render("mvc/views/", base="layout")

calculadora = form.Form(
    form.Textbox("num1", form.notnull, description="Nu_1:", class_="num1"),
    form.Textbox("num2", form.notnull, description="Nu_2:", class_="num2"),
    form.Button("=", style="background-color: #4caf50; color: #fff; padding: 10px; border: none; border-radius: 3px; cursor: pointer;"),
)

class Index:
    def GET(self):
        try:
            f = calculadora()
            return render.index(f)
        except Exception as e:
            print(f"Error 101 - index(): {e.args}")
            return "mal ):"

    def POST(self):
        form_data = web.input()
        num1 = int(form_data.num1)
        num2 = int(form_data.num2)
        suma = num1 + num2
        return suma
