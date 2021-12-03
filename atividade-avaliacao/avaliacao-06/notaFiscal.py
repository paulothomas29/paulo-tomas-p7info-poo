"""
    Módulo notafiscal -
    Classe NotaFiscal -
        Atributos :
            id        - informado.
            codigo    - informado.
            data      - informado.
            cliente   - informado.
            items     - informado
            valornota - calculado.
"""
from datetime import datetime
from clienteNotaFiscal import Cliente
from itemNotaFiscal import ItemNotaFiscal

from flaskp import db


class NotaFiscal(db.Model):
    __table__ = "TB_NOTA_FISCAL"
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String)
    cliente = db.Column(db.String, db.ForeignKey("TB_CLIENTE.codigo"))
    data = db.Column(db.Datatime)
    valorNota = db.Column(db.Float)
    
    cliente = db.relationship('Cliente', foreign_keys=codigo)
    
    def __init__(self, Id, codigo, cliente):
        self._Id = Id
        self._codigo = codigo
        self._cliente = cliente
        self._data = datetime.today()
        self._itens = []
        self._valorNota = 0.0

    def setCliente(self, cliente):
        if isinstance(cliente, Cliente):
            self._cliente = cliente
            return self._cliente

    def adicionarItem(self, item):
        if isinstance(item, ItemNotaFiscal):
            self._itens.append(item)

    def calcularNotaFiscal(self):
        valor = 0.0
        for item in self._itens:
            valor +=  item._valorItem
        self.valorNota = valor

    def imprimirNotaFiscal(self):
        print(f'''---------------------------------------------------------------------------------------------------
NOTA FISCAL \t\t\t\t {self._data}
Cliente: {self._cliente._codigo}\t\t\t\t Nome: {self._cliente._nome}
CPF/CNPJ: {self._cliente._cnpjcpf}
---------------------------------------------------------------------------------------------------
ITENS
---------------------------------------------------------------------------------------------------
Seq                        Descrição                           QTD   Valor Unit         Preço
---- -------------------------------------------------------- ----- ------------ ------------------''')
        for c in range(0, 3):
            print('{0:<17}{1:^34}{2:^28}{3:<8}{4}'.format(self._itens[c].getSequencial(),  self._itens[c].getDescricao(), self._itens[c].getQuantidade(), self._itens[c].getValorUnitario(), self._itens[c].getvalorItem()))

        print('Valor Total:', self.valorNota)