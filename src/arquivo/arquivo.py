'''
Created on 25 de nov de 2016

@author: amanda
'''


class Arquivo(object):
    
    def __init__(self):
        pass
    
    def ler_arquivo(self, arquivo):
        
        linhas = arquivo.readlines()
        
        transacoes = list()
        
        for line in linhas:
            transacoes.append(set(line.rstrip('\r\n').split(";")))
                        
        return transacoes