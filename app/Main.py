print("¡Hola! Bienvenido a este nuevo software de PQR S.A..")
print("Siga atentamente las instrucciones para generar su cotización de ventanas con nosotros.\n")

estilosVentanas = ["O", "XO", "OXO", "OXXO"]
acabadosAluminio = ["Pulido", "Lacado brillante", "Lacado mate", "Anodizado"]

#Solicitar al usuario el estilo de ventana y validarlo.
while True:
    tipoVentana = input("¿Qué tipo de ventanas desea? (O, XO, OXO, OXXO):")
    if tipoVentana in estilosVentanas:
        break 
    else:
        print("El estilo seleccionado no es válido. Por favor, ingrese una de las opciones: O, XO, OXO, OXXO.")

#Solicitar al usuario el acabado del aluminio y validarlo.
print("Listado de acabados disponibles para el aluminio:")
print("1. Pulido.")
print("2. Lacado brillante.")
print("3. Lacado mate.")
print("4. Anodizado.")
tipoAcabado = int(input("\n¿Qué tipo de acabado desea para el aluminio?:"))

print(f"Ha seleccionado: {acabadosAluminio[tipoAcabado]}")