from Ventana import Ventana

"""#Solicitar al usuario el estilo de ventana y validarlo.
while True:
    tipoVentana = input("¿Qué tipo de ventanas desea? (O, XO, OXO, OXXO):")
    if tipoVentana in estilosVentanas:
        break 
    else:
        print("El estilo seleccionado no es válido. Por favor, ingrese una de las opciones: O, XO, OXO, OXXO.\n")
        """


"""
#Solicitar al usuario el acabado del aluminio y validarlo.
while True:
    print("Listado de acabados disponibles para el aluminio:")
    print("1. Pulido.")
    print("2. Lacado brillante.")
    print("3. Lacado mate.")
    print("4. Anodizado.")
    tipoAcabado = 0

    try:
        tipoAcabado = int(input("\n¿Qué tipo de acabado desea para el aluminio?:"))  
    except ValueError:
        print("Valor incorrecto, debe ser un número 1-4.")

    
    if tipoAcabado >= 1 and tipoAcabado <= 4:
        print(f"Ha seleccionado: {acabadosAluminio[tipoAcabado - 1]}")
        break 
    else:
        print("El acabado seleccionado no es válido. Por favor, ingrese una de las opciones dadas.\n")
"""

class Main:
    def __init__(self):
        print("¡Hola! Bienvenido a este nuevo software de PQR S.A..")
        print("Siga atentamente las instrucciones para generar su cotización de ventanas con nosotros.")

    def run(self):
        # Aquí va el código principal de tu programa
        print()
        #Ventana(ancho, largo, estilo, acabadoAluminio, tipoVidrio, vidrioEsmerilado)
        miVentana = Ventana(12, 15, 1, 1, 1, False)
        print(f"Aluminio: ${miVentana.calcularCostoAluminio()}")
        print(f"Vidrio: ${miVentana.calcularValorVidrio()}")
        print(f"Valor de las {miVentana.esquinas} esquinas es de: ${miVentana.calcularValorEsquinas()}")
        print(f"Valor total: ${miVentana.calcularValor()}")

if __name__ == "__main__":
    app = Main()
    app.run()