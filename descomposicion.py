
from importlib.util import module_for_loader


class Automovil:

    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color 
        self._estado = 'en_reposo'
        self._estado_luces = 'apagadas'
        self._estado_puertas = 'cerradas'
        self._motor = Motor(cilindros=4)
        
    def acelerar(self, tipo='despacio'):
        if tipo == 'rapida':
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(3)

        self._estado = 'en_movimiento'

    def prender_luces(self, potencia='bajas'):
        if potencia == 'altas':
            self._luces.prender(2)
        else:
            self._luces.prender(1) 

        self._estado_luces = 'prendidas'

    def abrir_puerta(self, seguro_de_niños=False):
        if seguro_de_niños == False:
            self._puerta.abrir()
            self._estado_puertas = 'abierto'
        else:
            print('El seguro de niños esta activado')
            self._estado_puertas = 'cerrado'


class Motor:

    def __init__(self, cilindros, tipo='gasolina'):
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0

    def inyecta_gasolina(self, cantidad):
        pass

class Luces: 
    def __init__(self, color):
        self.color = color
    
    def prender(self, potencia):
        pass

class Puerta:
    def __init__(self, color):
        self.color = color

    def abrir(self, seguro_de_niños):
        pass