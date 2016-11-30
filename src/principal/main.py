'''
Created on 25 de nov de 2016

@author: amanda e flavio
'''
from arquivo.arquivo import Arquivo
from apriori.apriori import Apriori

if __name__ == '__main__':
    
    f = open("q1.3.csv", 'rb')
    transacoes = Arquivo().ler_arquivo(f)
    Apriori().apriori(transacoes, 0.01, 0.3)