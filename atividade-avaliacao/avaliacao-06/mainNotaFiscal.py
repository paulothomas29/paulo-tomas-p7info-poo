"""
  Módulo main - instancia objetos de classes definidas em
                módulos do pacote projeto01.
"""
from clienteNotaFiscal import Cliente
from itemNotaFiscal import ItemNotaFiscal
from notaFiscal import NotaFiscal
from produto import Produto


def main():
    cli = Cliente(1, "Jose Maria", 100, "200.100.345-34")

    p1 = Produto(1, 100, "Arroz Agulha", 5.5)
    it1 = ItemNotaFiscal(1, 1, 10, p1)

    p2 = Produto(2, 200, "Feijao Mulatinho", 8.5)
    it2 = ItemNotaFiscal(2, 2, 10, p2)

    p3 = Produto(3, 300, "Macarrão Fortaleza", 4.5)
    it3 = ItemNotaFiscal(3, 3, 10, p3)

    nf = NotaFiscal(1, 100, cli)

    nf.adicionarItem(it1)

    nf.adicionarItem(it2)

    nf.adicionarItem(it3)

    nf.calcularNotaFiscal()

    print("Valor Nota Fiscal= " + str(nf.valorNota))

    nf.imprimirNotaFiscal()

if __name__ == '__main__':
    main()