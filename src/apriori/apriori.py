'''
Created on 25 de nov de 2016

@author: amanda
'''
from itertools import combinations , permutations

class Apriori(object):
    '''
    classdocs
    '''
    
    def __init__(self):
        pass
    
    def calcular_frequencia(self, item, transacoes):
        cont = float()
        for transacao in transacoes:
            if(item.issubset(transacao)):
                cont+=1
        return cont/len(transacoes)
        
    def itens_frequentes(self, transacoes, suporte):
        itens = set()
        
        for transacao in transacoes:
            itens = itens.union(set(transacao)) 
        
        itens_frequencia = dict()
        itens_frequentes = set()
        
        frequencia = float()
        
        for item in itens:
            frequencia = self.calcular_frequencia(set([item]), transacoes)
            if(frequencia >= suporte):
                itens_frequencia[item]=frequencia;
                itens_frequentes.add(item)    
            
        return itens_frequencia, itens_frequentes
    
    
    def gerar_candidatos(self, itens_frequentes, k, transacoes, suporte):
        itens_candidatos = list()
        
        for itens in combinations(itens_frequentes, k):
            if(self.calcular_frequencia(set(itens), transacoes) >= suporte):
                itens_candidatos.append(list(itens))
            
        return itens_candidatos
    
    def conjunto_itens_frequentes(self, itens_frequentes_k):
        conjunto = set()
        
        for item_frequente in itens_frequentes_k:
            conjunto = conjunto.union(set(item_frequente))
        
        return list(conjunto)
        
    def atualizar_dicionario(self, itens_candidatos, itens_frequencia, transacoes):
        for item in itens_candidatos:
            itens_frequencia[str(item)]=self.calcular_frequencia(set(item), transacoes)
        
    def split_lista(self, itens):
        
        combinacoes = list()
        
        for combs in (combinations(itens, r) for r in range(len(itens)+1))  :
            for comb in combs:
                diff = list(set(itens[:]) - set(comb))
#                 print diff
#                 print list(comb)
                if(diff != [] and list(comb) != []):
                    combinacoes.append([diff, list(comb)])
                    
        return combinacoes
            
    def gerar_regras(self, itens_set_frequentes, itens_frequencia, confianca, transacoes):
        for itens in itens_set_frequentes:
            regras_candidatas = self.split_lista(itens)
            for [imp, conc] in regras_candidatas:
                suporte_regra = self.calcular_frequencia(set(imp+conc), transacoes)
                suporte_imp = self.calcular_frequencia(set(imp), transacoes)
                suporte_conc = self.calcular_frequencia(set(conc), transacoes)
                if(suporte_regra/suporte_imp > confianca):
                    print imp, "("+str(("%.2f" % round(suporte_imp,2)))+")","->", conc, "("+str(("%.2f" % round(suporte_conc,2)))+")", "["+str(("%.2f" % round(suporte_regra/suporte_imp,2)))+"]"
                
                
    def apriori(self, transacoes, suporte, confianca):
        
        itens_frequencia, itens_frequentes = self.itens_frequentes(transacoes, suporte)
        itens_frequentes_k = itens_frequentes
        itens_set_frequentes = list()
        
        k = 2
        
        while(len(itens_frequentes_k) > 0):
            itens_candidatos = self.gerar_candidatos(itens_frequentes_k, k, transacoes, suporte)
            itens_set_frequentes = itens_set_frequentes + itens_candidatos
            itens_frequentes_k = self.conjunto_itens_frequentes(itens_candidatos)
            self.atualizar_dicionario(itens_candidatos, itens_frequencia, transacoes)
            print k
            k+=1
        
        self.gerar_regras(itens_set_frequentes, itens_frequencia, confianca, transacoes)