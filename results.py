from restaurant import Restaurant
from exceptions import InvalidObjectTypeException

class No:
    '''
    Classe de nó para a pilha de resultados
    '''
    def __init__(self,carga:'Restaurant' = None, prox:'No' = None):
        self.carga=carga
        self.prox=prox
    
    @property
    def carga(self):
        return self.__carga
    
    @carga.setter
    def carga(self,c):
        if not isinstance(c,Restaurant) and c is not None: raise InvalidObjectTypeException()
        self.__carga=c
    
    @property
    def prox(self):
        return self.__prox
    
    @prox.setter
    def prox(self,p):
        if not isinstance(p,No) and p is not None: raise InvalidObjectTypeException()
        self.__prox=p

    def __str__(self):
        return self.carga.__str__()

class Results:
    '''
    Classe baseada na estrutura de dados pilha que armazena os resultados da pesquisa.
    '''
    def __init__(self,topo:'No'=None):
        self.topo=topo
    
    def add(self,no:'No'):
        
        if not self.topo: 
            self.topo=no
        else:
            atual=self.topo
            while atual.prox:
                atual=atual.prox
            atual.prox=no

    def listar(self):
        if not self.topo: return 'lista vazia'

        i=1
        atual=self.topo
        print(atual)
        while atual.prox and i < 5:
            atual=atual.prox
            print(atual)
            i+=1
            
if __name__ == '__main__':
    from restaurant_importer import restaurant_importer

    restaurantes=restaurant_importer()

    pilha=Results()

    for r in restaurantes:
        pilha.add(No(r))
    
    pilha.listar()