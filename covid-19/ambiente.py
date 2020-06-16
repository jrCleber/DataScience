#!/usr/bin/env python
# coding: utf-8

# In[22]:


from os import chdir, listdir
from pathlib import Path as path
from shutil import copy as cp
from meta import Meta
from datetime import datetime as dt

class DSAmbiente:
    def __init__(self):
        self._diretorios = '001 - Dados Originais', '002 - Dados Preparados', '003 - Analises', '004 - Dados Upload', '005 - Insigths', '006 - Final', '_versionamento_'
        self._path = path.home() / 'Desktop' / 'Python'
        self._dirwork = 'Analises'
        self._criacao = self.get_path()/self.get_dirwork()
        self._desktop = path.cwd()
            
    def get_path(self):
        return self._path    
    def set_path(self, valor):
        self._path = valor        
    def get_dirwork(self):
        return self._dirwork    
    def set_dirwork(self, valor):
        self._dirwork = valor    
    def get_dir(self):
        return self._diretorios    
    def set_dir(self, valor):
        self._diretorios = valor
    def get_criacao(self):
        return self._criacao
    def set_criacao(self, valor):
        self._criacao = valor
    def set_desktop(self, valor):
        self._desktop = valor
    def get_desktop(self):
        return self._desktop
    
    #função que constroi oambiente de trabalho para DataScience
    def construcao(self, file):
        ambiente = None
        if not path.is_dir(self.get_criacao()):
            print('Path inesistente')
            print('Criando Path...')
            try:
                path.mkdir(self.get_criacao())
                ambiente = True
            except FileNotFoundError as e:
                print('[WinError 3] O sistema não consegue encontrar o caminho especificado em:')
                print(self.get_criacao())
                ambiente = False
        else:
            ambiente = True
        if file == None or file == '':
            print('Não há datasets alocados neste ambiente')
            ambiente = True
        if ambiente:
            chdir(self.get_criacao())
            for pasta in self.get_dir():
                if not path(self.get_criacao() / pasta).exists():
                    path.mkdir(self.get_criacao() / pasta)
                if pasta == self.get_dir()[0]:
                    local = self.get_criacao() / self.get_dir()[0]
                    chdir(local)
                    self.copy_file(file, local)
                    
                elif pasta == self.get_dir()[1]:
                    local = self.get_criacao() / self.get_dir()[1]
                    chdir(local)
                    self.copy_file(file, local)                        
        chdir(self.get_desktop())
        print('Ambiente criado com sucesso em: \n', self.get_criacao())
    
    #função que copia um um arquivo de um dataset expecífico e cola dentro do diretório de trabalho
    def copy_file(self, file, local):
        try:
            cp(file, local)
        except FileNotFoundError as e:
            print(type(e))
            print('[WinError 3] O sistema não consegue encontrar o caminho especificado em:\n', file)
            print('Não foi possível copiar o arquivo para:\n', local)
        except PermissionError as e:
            print(type(e))
            print('Permisao de acesso ao diretorio negada')
    
    #função que retorna o path de um aqrquivo em um diretório específico
    def local_file(self, local_data):
        chdir(local_data)         
        print('SELECIONE O DATASET:\n'+'_'*60)
        print(path.cwd())
        #print('\n')
        list_file = listdir()
        for i in range(len(list_file)):
            print('(%i) para para o Dataset: %s'%(i,list_file[i]))            
        print('_'*60)
        chdir(self.get_desktop())
        while True:
            try:
                print('-'*60)
                return local_data / list_file[int(input('Escolha: '))]
            except ValueError as e:
                print(type(e))
                print('Valor inválido')
            except IndexError as e:
                print(type(e))
                print('Índice inválido')
    """
    função que verifica se o ambiente fora criado e 
    retorna o path do arquivo de trabalho que foi copiado para dentro do ambiente de trabalho
    """
    def file_data_ambiente(self):
        dir_file = self.get_criacao() / self.get_dir()[1]
        if not path(dir_file).exists():
            print('E nescessário criar o ambiente.\nUtilize o método: def construcao(file), para criar o ambiente.')
        else:
            chdir(dir_file)
            return self.local_file(path.cwd())

#DIREITOS
meta = Meta()
meta.set_meta('datetime', dt(2020,6,14,8,41))

