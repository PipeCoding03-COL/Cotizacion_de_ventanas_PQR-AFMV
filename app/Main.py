from Ventana import Ventana

class Main:

    def __init__(self):
        print("¡Hola! Bienvenido a este nuevo software de PQR S.A..")
        print("Siga atentamente las instrucciones para generar su cotización de ventanas con nosotros.\n")

    def run(self):
        ancho = largo = estilo = acabadoAluminio = tipoVidrio = cantidad = 0
        # Aquí va el código principal de tu programa
        #Ventana(ancho, largo, estilo, acabadoAluminio, tipoVidrio, vidrioEsmerilado)

        #miVentana = Ventana(12, 15, 1, 1, 1, False, 80) #Ejemplo del documento (tipo O)
        #miVentana = Ventana(25, 30, 2, 3, 3, True, 120) #Ejemplo propio #1
        #miVentana = Ventana(25, 30, 2, 3, 3, False, 90) #Ejemplo propio (Alternativa #1)
        #miVentana = Ventana(25, 30, 4, 3, 3, False, 110) #Ejemplo propio (Alternativa #2)

        #miVentana.imprimirDatosVentana()
        #miVentana.calcularValorDeLasNaves()

        #Solicitar al usuario el ancho de la ventana y validarlo.
        while True:
            try:
                ancho = float(input("Ancho de la ventana (cm): ") )

                if ancho >= 10:
                    break 
                else:
                    print("La opción seleccionada no es válida, pues es menor de lo permitido. Por favor, intente nuevamente.\n")
            except ValueError:
                print("Valor incorrecto, debe ser un número 10-n.")

        #Solicitar al usuario el alto de la ventana y validarlo.
        while True:
            try:
                largo = float(input("Alto de la ventana (cm): ") )

                if largo >= 10:
                    break 
                else:
                    print("La opción seleccionada no es válida, pues es menor de lo permitido. Por favor, intente nuevamente.\n")
            except ValueError:
                print("Valor incorrecto, debe ser un número 10-n.")

        #Solicitar al usuario el estilo de ventana y validarlo.
        while True:
            print("Tipos de ventana:")
            print("1. O")
            print("2. XO")
            print("3. OXO")
            print("4. OXXO")
            estilo = 0

            try:
                estilo = int(input("¿Qué tipo de ventana desea?: ") )
            except ValueError:
                print("Valor incorrecto, debe ser un número 1-4.")
            
            if estilo >= 1 and estilo <= 4:
                break 
            else:
                print("La opción seleccionada no es válida. Por favor, ingrese una de las opciones dadas.\n")

        #Solicitar al usuario el acabado del aluminio y validarlo.
        while True:
            print("\nListado de acabados disponibles para el aluminio:")
            print("1. Pulido.")
            print("2. Lacado brillante.")
            print("3. Lacado mate.")
            print("4. Anodizado.")
            acabadoAluminio = 0

            try:
                acabadoAluminio = int(input("\n¿Qué tipo de acabado desea para el aluminio?: "))  
            except ValueError:
                print("Valor incorrecto, debe ser un número 1-4.")

            
            if acabadoAluminio >= 1 and acabadoAluminio <= 4:
                break 
            else:
                print("El acabado seleccionado no es válido. Por favor, ingrese una de las opciones dadas.\n")

        #Solicitar al usuario el tipo de vidrio y validarlo.
        while True:
            print("\nListado de tipos de vidrio disponibles para la ventana:")
            print("1. Transparente.")
            print("2. Bronce.")
            print("3. Azul.")
            tipoVidrio = 0

            try:
                tipoVidrio = int(input("\n¿Qué tipo de vidrio desea?: "))  
            except ValueError:
                print("Valor incorrecto, debe ser un número 1-3.")

            
            if tipoVidrio >= 1 and tipoVidrio <= 3:
                break 
            else:
                print("El acabado seleccionado no es válido. Por favor, ingrese una de las opciones dadas.\n")

        #Preguntar al usuario si desea que el vidrio sea esmerilado o no.
        while True:
            print("\n¿Desea que el vidrio sea esmerilado?:")
            print("1. Sí.")
            print("2. No.")

            try:
                vidrioEsmerilado = int(input("\n¿Desea que el vidrio sea esmerilado?: "))
                break
            except ValueError:
                print("Valor incorrecto, debe ser un número 1 o 2.")


        #Solicitar al usuario la cantidad de ventanas a fabricar.
        while True:
            try:
                cantidad = int(input("Cantidad de ventanas a fabricar: ") )

                if cantidad >= 10:
                    break 
                else:
                    print("La opción seleccionada no es válida, pues es menor de lo permitido. Por favor, intente nuevamente.\n")
            except ValueError:
                print("Valor incorrecto, debe ser un número 10-n.")
        
        ventana = Ventana(ancho, largo, estilo, acabadoAluminio, tipoVidrio, vidrioEsmerilado, cantidad)

        ventana.imprimirDatosVentana()

        ventana.imprimirDatosVentana()
        ventana.calcularValorDeLasNaves()

        #miVentana = Ventana(12, 15, 1, 1, 1, False, 80) #Ejemplo del documento (tipo O)
        #miVentana.imprimirDatosVentana()
        #miVentana.calcularValorDeLasNaves()

if __name__ == "__main__":
    app = Main()
    app.run()
    