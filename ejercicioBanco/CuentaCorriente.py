from .CuentaBancaria import CuentaBancaria

class CuentaCorriente(CuentaBancaria):
    def __init__(self, _titular, _cbu, saldo_inicial, limite_descubierto=500):
        super().__init__(_titular, _cbu, saldo_inicial)
        self.limite_descubierto=limite_descubierto 

    def extraer(self,monto):
        if monto <=0:
           raise ValueError ("no se puede extraer un monto negativo o igual a cero")
        if monto > self._saldo + self.limite_descubierto:
            raise ValueError ("no se puede extraer un monto superior al saldo")
        self._saldo=self._saldo-monto
        print(f"Extraccion por ${monto} realizada. Saldo restante: ${self._saldo} (Limite desc: ${self.limite_descubierto})")