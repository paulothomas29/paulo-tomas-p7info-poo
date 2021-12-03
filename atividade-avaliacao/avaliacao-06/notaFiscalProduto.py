"""
"""

from notaFiscal import NotaFiscal
from produto import Produto


class NotaFiscal_Produto():

    def _init_(self):
        self._notasFiscais = []
        self._produtos = []

    def adicionarNotaProduto(self, nota, produto):
        if isinstance(nota, NotaFiscal) and isinstance(produto, Produto):
            self._notasFiscais.append(nota)
            self._produtos.append(produto)