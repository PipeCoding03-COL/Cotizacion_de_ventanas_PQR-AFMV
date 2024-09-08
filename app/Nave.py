class Nave:
    valorVidrioEsmerilado = 5.20
    valorChapas = 16200
    valorEsquinas = 4310

    def _init_(self, ancho, largo, tipo):
        self.ancho = ancho
        self.largo = largo
        self.tipo = tipo

    def calcularCostoAluminio(self, costoAluminioPulidoPorM):
        perimetro = 2 * (self.ancho - 6 + self.largo - 6) #Descontar las esquinas
        return (perimetro / 100) * costoAluminioPulidoPorM
    
    def calcularValorVidrio(self, valorPorCm2, vidrioEsmerilado):
        areaVidrio = (self.ancho - 3) * (self.largo - 3)
        valorVidrio = valorPorCm2 * areaVidrio

        if vidrioEsmerilado:
            valorVidrio += (self.valorVidrioEsmerilado * areaVidrio)
        
        return valorVidrio
    
    def calcularValorEsquinas(self):
        return self.valorEsquinas * 4
    
    def calcularValor(self):
        valor = self.calcularCostoAluminio() + self.calcularValorVidrio() + self.calcularValorEsquinas()

        if self.tipo == "X":
            valor += self.valorChapas

        return valor

    def calcularPerimetro(self):
        return 2 * (self.ancho + self.largo)

    def calcularAreaVidrio(self):
        # El vidrio es 1.5 cm más pequeño en cada lado
        return (self.ancho - 3) * (self.largo - 3)