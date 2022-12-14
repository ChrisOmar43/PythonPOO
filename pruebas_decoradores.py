'''def funcion_decoradora(funcion):
	def wrapper():
		print("Este es el último mensaje...")
		funcion()
		print("Este es el primer mensaje ;)")
	return wrapper

def zumbido():
	print("Buzzzzzz")

zumbido = funcion_decoradora(zumbido)

zumbido()

class CasillaDeVotacion:
    
    def __init__(self, identificador, pais):
        self._identificador = identificador
        self._pais = pais
        self._region = None

    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, region):
        if region in self._pais:
            self._region = region
        else:
            raise ValueError(f'La region {region} no esta en la lista')


casilla = CasillaDeVotacion(123,['Mexico','Morelos'])
print(casilla.region)
casilla.region = 'Mexico'
print(casilla.region)'''

import re

class Persona:
    """Abstracción del objeto Persona de la Lista Nominal"""

    def __init__(self, nombre, apellido_paterno, apellido_materno):
        self.__nombre = nombre
        self.__apellido_paterno = apellido_paterno
        self.__apellido_materno = apellido_materno
        self.__numero_credencial_elector = None 

    @property
    def nombre(self):
        """Regresa el nombre en mayúsculas"""
        return self.__nombre.upper()
    
    @property
    def apellido_paterno(self):
        """Regresa el apellido_paterno en mayúsculas"""
        return self.__apellido_paterno.upper()

    @property
    def apellido_materno(self):
        """Regresa el apellido_materno en mayúsculas"""
        return self.__apellido_materno.upper()

    @property
    def numero_credencial_elector(self):
        """Regresa numero_credencial_elector"""
        return self.__numero_credencial_elector

    @numero_credencial_elector.setter
    def numero_credencial_elector(self, numero_credencial_elector):
        """Método para asignar numero_credencial_elector
        
        Sólo se permiten caracteres alfanúmericos.
        Letras sólo en mayúscula.
        Exactamente 18 caracteres.
        """
        if re.match(r'[A-Z0-9]{18}$', numero_credencial_elector):
            self.__numero_credencial_elector = numero_credencial_elector
        else:
            raise ValueError('El numero de la credencial de elector {}, no es válido'.format(
                numero_credencial_elector
        ))


if __name__ == "__main__":
    persona = Persona('Juana','López','lugo')
    print(persona.apellido_paterno)
    print(persona.apellido_materno)
    print(persona.nombre)

    persona.numero_credencial_elector = 'JLLBCABDABC22C669L'
    print(persona.numero_credencial_elector)