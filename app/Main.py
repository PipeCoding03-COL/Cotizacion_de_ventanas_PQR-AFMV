print("¡Hola! Bienvenido a este nuevo software de PQR S.A..")
print("Siga atentamente las instrucciones para generar su cotización de ventanas con nosotros.\n")

#Solicitar el estilo de ventana al usuario y validarlo.
estilosVentanas = ["O", "XO", "OXO", "OXXO"]
while True:
    tipoVentana = input("¿Qué tipo de ventanas desea?: (O, XO, OXO, OXXO)")
    if tipoVentana in estilosVentanas:
        print("Correcto. Continuemos.")
    else:
        print("El estilo seleccionado no es válido. Por favor, ingrese una de las opciones: O, XO, OXO, OXXO.")