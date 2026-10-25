from .CuentaBancaria import CuentaBancaria

class CuentaCheque(CuentaBancaria):
    def __init__(self, _titular, _cbu, saldo_inicial, costo_emision=50):
        super().__init__(_titular, _cbu, saldo_inicial)
        self.costo_emision=costo_emision

    def extraer(self,monto):
        if monto <=0:
           raise ValueError ("no se puede extraer un monto negativo o igual a cero")
        if monto + self.costo_emision > self._saldo:
            raise ValueError ("no se puede extraer un monto superior al saldo")
        self._saldo=self._saldo-monto-self.costo_emision
        print(f"Cheque emitido por ${monto} (Comision: ${self.costo_emision}). Saldo restante: ${self._saldo}")