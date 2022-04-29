import csv
from clasePlan import Plan

class Manejador:
    __lista = []

    def __init__(self):
        self.__lista = []

    def agregarPlan(self, unPlan):
        if type(unPlan) == Plan:
            self.__lista.append(unPlan)

    def __str__(self):
        s = ''
        for plan in self.__lista:
            s += str(plan)+'\n\n'
        return s    

    def cargarLista(self):
        #band = True
        archivo = open('planes.csv')
        reader = csv.reader(archivo, delimiter = ';')
        for fila in reader:
            unPlan = Plan(int(fila[0]),fila[1], fila[2], float(fila[3]))
            self.agregarPlan(unPlan)
        archivo.close()

    def calcularValorCuotas(self):
        i = 0
        while i < len(self.__lista):
            self.__lista[i].calcularValorCuota()
            i+=1


    def actualizarImportes(self):
        i = 0
        while i < len(self.__lista):
            print('\n')
            print('Codigo de plan: {} Modelo: {} Version: {}  Importe: {}\n'. format(self.__lista[i].getCodigoPlan(), self.__lista[i].getModeloVehiculo(), self.__lista[i].getVersionVehiculo(), self.__lista[i].getValorVehiculo()))
            valor_viejo = float(input('Ingrese el importe actual del vehiculo: '))
            self.__lista[i].ActualizarValor(valor_viejo)
            i+=1

    def mostrarDatosValor(self, unValor):
        if type(unValor) == float:
            i = 0
            while i < len(self.__lista):
                if self.__lista[i].getValorCuota() < unValor:
                    print('\n')
                    print('Codigo de plan: {} Modelo: {} Version: {}\n'. format(self.__lista[i].getCodigoPlan(), self.__lista[i].getModeloVehiculo(), self.__lista[i].getVersionVehiculo()))
                    i+=1
                else:
                    i+=1

    def mostrarCantidadPagar(self):
        codigo_plan = int(input('Ingrese el codigo de un plan: '))
        i = 0
        encontro = False
        while i < len(self.__lista) and not encontro:
            if self.__lista[i].getCodigoPlan() == codigo_plan:
                valor_licitar = (Plan.getCantidadCuotas() * self.__lista[i].getValorCuota())     
                print('\n')
                print('El monto que se debe abonar para licitar el vehiculo {} es {}'. format(self.__lista[i].getModeloVehiculo(), valor_licitar))     
                encontro = True
            else:
                i+=1
        if not encontro:
            print('No se encontro el plan')
            

               





           
















            