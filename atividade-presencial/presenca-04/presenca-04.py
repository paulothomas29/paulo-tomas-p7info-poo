class Fila():
    
    def __init__(self):
        self.fila = []
        
    def inserir(self, elemento):
        self.fila.append(elemento)
        
    def retirar(self):
        if len(self.fila) > 0:
            del self.fila[0]
    
    def vazia(self):
        return self.fila == []
    
    def mostrarFila(self):
        print (self.fila)
        
pt = Fila()

for p in range(3):
    pt.inserir(p)
    
pt.mostrarFila()
pt.inserir(3)
pt.mostrarFila()
pt.retirar()
pt.mostrarFila()

for p in range(5):
    pt.retirar()

pt.mostrarFila()