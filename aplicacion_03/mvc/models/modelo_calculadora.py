import web

class ModeloCalculadora:
    def __init__(self):
        pass

    def calcular(self, num1, num2):
        try:
            # Realiza la operación de suma
            resultado = float(num1) + float(num2)
            return resultado
        except Exception as e:
            print(f"Error en el cálculo: {e}")
            return None
