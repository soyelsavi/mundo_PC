class DispositivosEntrada:
    def __init__ (self, tipo,marca):
        self._tipo = tipo
        self._marca = marca
    
    def get_tipo (self):
        return self._tipo
    def set_tipo (self, tipo):
        self._tipo = tipo
        
    def get_marca(self):
        return self._marca
    def set_marca(self,marca):
        self._marca = marca 
        
    def __str__(self):
        mensaje ="Tipo: "+ self.tipo + ", Marca: "+ self._marca
        
    