class Hotel:
    def __init__(self, numero_maximo_de_huespedes, lugares_de_estacionamiento):
        self.numero_maximo_de_huespedes = numero_maximo_de_huespedes
        self.lugares_de_estacionamiento =lugares_de_estacionamiento
        self.huespedes = 0

hotelMisHuevos = Hotel(numero_maximo_de_huespedes=50, lugares_de_estacionamiento=20)
print(hotelMisHuevos.numero_maximo_de_huespedes)
