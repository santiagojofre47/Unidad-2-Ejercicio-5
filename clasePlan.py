class Plan:
    __codigoPlan = None
    __modelo = None
    __versionVehiculo = None
    __valor = None
    __valorCuota = None
    cantidadCuotas = 84
    cantidadNecesaria = 15

    def __init__(self, codigo = None, modelo = None, version = None, valor = None, valorcuota = 0):
        self.__codigoPlan = codigo
        self.__modelo = modelo
        self.__versionVehiculo = version
        self.__valor = valor
        self.__valorCuota = valorcuota

    def getCodigoPlan(self):
        return self.__codigoPlan    

    def getValorVehiculo(self):
        return self.__valor

    def getModeloVehiculo(self):
        return self.__modelo

    def getVersionVehiculo(self):
        return self.__versionVehiculo

    def ActualizarValor(self, valor_actual):
        if type(valor_actual) == float:
            if self.getValorVehiculo() == valor_actual:
                nuevo_valor = float(input('Ingrese el nuevo valor: '))
                self.__valor = nuevo_valor
            else:
                print('Valor ingresado incorrecto') 

    def calcularValorCuota(self):
        valor = (self.__valor/Plan.getCantidadCuotas())+(self.__valor*0.10)
        self.__valorCuota = valor

    def getValorCuota(self):
        return float(self.__valorCuota)

    def __str__(self):
        return 'Codigo de plan: {}\nModelo Vehiculo: {}\nVersion: {}\nImporte: {}\nImporte Cuota: {}'. format(self.__codigoPlan,self.__modelo,self.__versionVehiculo,self.__valor, self.__valorCuota)


    #Metodos de clase
    @classmethod
    def getCantidadCuotas(cls):
        return cls.cantidadCuotas

    @classmethod
    def setCantidadCuotas(cls, cantidad):
        cls.cantidadCuotas = cantidad

    @classmethod
    def setCantidadCuotasNecesarias(cls, cantidad):
        cls.cantidadNecesaria = cantidad












