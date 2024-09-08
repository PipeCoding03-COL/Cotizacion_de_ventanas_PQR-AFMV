class Ventana:
    #O = No se puede abrir // X = Sí se puede abrir (debe llevar chapa)
    estilosVentanas = ["O", "XO", "OXO", "OXXO"]
    #Acabados del aluminio y su coste por metro lineal
    acabadosAluminio = [["Pulido", "Lacado brillante", "Lacado mate", "Anodizado"],
                        [50700, 54200, 53600, 57300]]
    #Tipos de vidrios y su precio por centímetro cuadrado
    tiposDeVidrio = [["Transparente", "Bronce", "Azul"],
                   [8.25, 9.15, 12.75]]
    #Un vidrio esmerilado tiene un valor de $5.20 adicionales
    valorVidrioEsmerilado = 5.20
    valorChapas = 16200
    valorEsquinas = 4310

    def __init__(self, ancho, largo, estilo, acabadoAluminio, tipoVidrio, vidrioEsmerilado):
        self.ancho = ancho
        self.largo = largo
        self.estilo = estilo
        self.acabadoAluminio = acabadoAluminio
        self.tipoVidrio = tipoVidrio
        self.vidrioEsmerilado = vidrioEsmerilado

    def imprimirDatosVentana(self):
        print(f"Ancho: {self.ancho} cm")
        print(f"Largo: {self.largo} cm")
        print(f"Estilo: {self.estilosVentanas[self.estilo - 1]}")
        print(f"Acabado del aluminio: {self.acabadosAluminio[0][self.acabadoAluminio - 1]}")
        print(f"Valor de ese acabado (por metro lineal): {self.acabadosAluminio[1][self.acabadoAluminio - 1]}")
        print(f"Tipo de vidrio: {self.tiposDeVidrio[0][self.tipoVidrio - 1]}")
        print(f"Valor de ese tipo de vidrio (por centímetro cuadrado): {self.tiposDeVidrio[1][self.tipoVidrio - 1]}")
        print(f"Vidrio esmerilado: {self.vidrioEsmerilado}")

    def calcularCantidadDeNaves(self):
        return len(self.estilosVentanas[self.estilo - 1])

    def calcularCostoAluminio(self):
        costoAluminioPulidoPorM = self.acabadosAluminio[1][self.acabadoAluminio - 1]
        perimetro = 2 * (self.ancho - 6 + self.largo - 6) #Descontar las esquinas
        return (perimetro / 100) * costoAluminioPulidoPorM

    def calcularValorVidrio(self):
        areaVidrio = (self.ancho - 3) * (self.largo - 3)
        valorPorCm2 = self.tiposDeVidrio[1][self.tipoVidrio - 1]
        valorVidrio = valorPorCm2 * areaVidrio

        if self.vidrioEsmerilado:
            valorVidrio += (self.valorVidrioEsmerilado * areaVidrio)
        
        return valorVidrio
    
    def calcularValorEsquinas(self):
        return self.valorEsquinas * self.calcularCantidadDeNaves() * 4

    def calcularValor(self):
        valor = self.calcularCostoAluminio() + self.calcularValorVidrio() + self.calcularValorEsquinas()

        return valor
    
    def calcularValorDeLasNaves(self):
        naves = self.calcularCantidadDeNaves()
        self.ancho /= naves
        valorAluminio = self.calcularCostoAluminio()
        valorVidrio = self.calcularValorVidrio()
        valorPorNave = valorAluminio + valorVidrio
        valorTotal = valorPorNave * naves
        valorTotal += self.estilosVentanas[self.estilo - 1].count("X") * self.valorChapas
        
        print(f"\nCantidad de naves: {naves}")
        print(f"Ancho de cada nave: {self.ancho}")

        print(f"\nCosto aluminio: ${valorAluminio}")
        print(f"Costo vidrio: ${valorVidrio}")
        print(f"Costo por nave: ${valorPorNave}")
        print(f"\nValor de las {naves} naves: {valorTotal}")

        return valorTotal