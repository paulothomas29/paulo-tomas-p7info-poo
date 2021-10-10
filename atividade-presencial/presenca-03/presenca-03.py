class Pilha():
    
    def __init__(self):
       self.pilha = []
       
    def adicionar(self, elemento):
       self.pilha.append(elemento)
    
    def retirar(self):
        if len(self.pilha) > 0:
            return self.pilha.pop(-1)
    
    def vazio(self):
        return self.pilha == []
    
    def mostrarPilha(self):
        print(self.pilha)
       
    
stack = Pilha()

for p in range(5):
    stack.adicionar(p)

stack.mostrarPilha()
stack.retirar()
stack.mostrarPilha()

for p in range(10):
    stack.retirar()

stack.mostrarPilha()