from clasePlan import Plan
from claseManejador import Manejador

class Menu:
    __opcion = 0

    def __init__(self, opcion = 0):
        self.__opcion = opcion

    def EjecutarA(self, unManejador):
        if type(unManejador) == Manejador:
            unManejador.actualizarImportes()
            print(unManejador)

    def EjecutarB(self, unManejador):
        if type(unManejador) == Manejador:
            valor = float(input('Ingrese un valor: '))
            unManejador.mostrarDatosValor(valor)

    def EjecutarC(self, unManejador):
        if type(unManejador) == Manejador:
            unManejador.mostrarCantidadPagar()

    def EjecutarD(self):
        cantidad = int(input('Ingrese la nueva cantidad de cuotas: '))
        Plan.setCantidadCuotas(cantidad)    


    def mostrarMenu(self, unManejador):
        if type(unManejador) == Manejador:
            salir = False
            print(' === Menu de opciones ===')    
            while not salir:
                print('\n')
                print('a- Actualizar importe de los vehiculos de cada plan')
                print('b- Mostrar datos de un plan cuyo importe sea inferior al de un importe ingresado')
                print('c- Mostrar importe que se debe pagar para licitar un determinado vehiculo')
                print('d- Modificar la cantidad de cuotas necesarias para licitar un vehiculo (para todos los planes)')
                print('e- salir')
                self.__opcion = input('Ingrese una opcion: ')
                
                if self.__opcion.lower() == 'a':
                    self.EjecutarA(unManejador)
                elif self.__opcion.lower() == 'b':
                    self.EjecutarB(unManejador)
                elif self.__opcion.lower() == 'c':
                    self.EjecutarC(unManejador)
                elif self.__opcion.lower() == 'd':
                    self.EjecutarD()
                elif self.__opcion.lower() == 'e':
                    salir = True    
                    print('Cerrado menu...')
                else:
                    print('ERROR: Opcion ingresada incorrecta!')      
                    input('Presione ENTER para continuar...')          