class Nave:
    def _init_(self, ancho, largo):
        self.ancho = ancho
        self.largo = largo
        self.valorEsquina = 4310
        self.valorChapa = 16200

    def calcularPerimetro(self):
        return 2 * (self.ancho + self.largo)

    def calcularAreaVidrio(self):
        # El vidrio es 1.5 cm más pequeño en cada lado
        return (self.ancho - 3) * (self.largo - 3)