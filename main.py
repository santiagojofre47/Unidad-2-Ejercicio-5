from claseManejador import Manejador
from clasePlan import Plan
from claseMenu import Menu

def test():
    print('Iniciando test...')
    unPlan = Plan(100,"Mercedez 02", "Version 1",1500000)
    print('=== Antes de calcular el valor de cuota ===\n')
    print(unPlan)
    unPlan.calcularValorCuota()
    print(' === Despues de calcular el valor de cuota ===\n')
    print(unPlan)
    unPlan.ActualizarValor(float(10000))#CASO INCORRECTO
    unPlan.ActualizarValor(float(unPlan.getValorVehiculo()))
    print(' === Despues de actualizar el valor del vehiculo === ')
    print(unPlan)
    print('Cerrando test...\n\n')


if __name__ == '__main__':
    test()
    unManejador = Manejador()
    unMenu = Menu()
    unManejador.cargarLista()
    unManejador.calcularValorCuotas()
    print(unManejador)
    unMenu.mostrarMenu(unManejador)