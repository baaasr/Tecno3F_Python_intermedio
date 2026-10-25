from abc import ABC, abstractmethod

class CuentaBancaria(ABC):
    def __init__(self, _titular, _cbu, saldo_inicial):
        self._titular=_titular
        self._cbu=_cbu
        self._saldo=saldo_inicial

    @property
    def saldo(self):
        return self._saldo

    @property
    def titular(self):
        return self._titular
    
    @property
    def cbu(self):
        return self._cbu
    
    @saldo.setter
    def saldo(self,valor):
        if valor <=0:
            raise ValueError("El valor indicado no puede ser negativo")
        self._saldo=valor

    def depositar(self, monto):
        if monto <=0:
           raise ValueError ("no se puede depositar un monto negativo") 
        self._saldo=(self._saldo+monto)

    def __str__(self):
        return f"[{self.__class__.__name__}] TITULAR: {self._titular} | CBU: {self._cbu} | SALDO: ${self._saldo}"
   
    @abstractmethod
    def extraer(self,monto):
        pass
    
        
    


        