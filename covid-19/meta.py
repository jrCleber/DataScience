# coding: utf-8

class Meta:
    def __init__(self):
        self._metadados = {
            '__author__' : 'Cleber Wilson',
            '__version__' : '1.0.0',
            '__license__' : 'Domínio público',
            '__copyright__'  : 'Copyright 2020 by Me',
            '__title__' : 'DataScience',
            '__email__' : 'email@dominio.com',
            '__status__' : 'Em produção',
            '__credits__' : ['Cleber Wilson'],
            '__url__' : 'https://github.com/jrCleber/python-para-dados'
        }
    def get_meta(self):
        return self._metadados
    def set_meta(self, indice, valor):
        self._metadados[indice] = valor