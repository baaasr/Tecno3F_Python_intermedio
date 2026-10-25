from .CuentaBancaria import CuentaBancaria

class CuentaAhorro(CuentaBancaria):
    def __init__(self, _titular, _cbu, saldo_inicial):
        super().__init__(_titular, _cbu, saldo_inicial)

    def extraer(self,monto):
        if monto <=0:
           raise ValueError ("no se puede extraer un monto negativo o igual a cero")
        if monto > self._saldo:
            raise ValueError ("no se puede extraer un monto superior al saldo")
        self._saldo=self._saldo-monto
        print(f"Extraccion por ${monto} realizada. Saldo restante: ${self._saldo}")

    def aplicar_interes(self):
        interes=self._saldo*0.001
        self._saldo = self._saldo +interes
        print(f"Interes mensual aplicado (+${interes}). Nuevo saldo: ${self._saldo}")
        