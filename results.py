from restaurant import Restaurant
from exceptions import InvalidObjectTypeException
from sorting_mechanisms import *

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
        self.numero=0

    def list_to_result(self,restaurants:list):
        '''
        Método que utiliza uma lista para gerar os resultados
        '''

        sorted_restaurants=self.__sorting(restaurants)

        for r in sorted_restaurants[::]:
            self.__add(No(r))



    def list(self):
        if not self.topo: return 'lista vazia'

        atual=self.topo
        pos_atual=1
        print(atual)

        while atual.prox and pos_atual < 5:
            atual=atual.prox
            print(atual)
            #pos_atual+=1    # garante que apenas os 5 primeiros irão ser filtrados
    


    def __add(self,no:'No'):
        '''
        Método privado de adiação de um nó nos resultados
        '''
        if not self.topo: 
            self.topo=no
        else:
            atual=self.topo
            while atual.prox:
                atual=atual.prox
            atual.prox=no


    def __sorting(self,restaurants):
        '''
        Método privado que ordena a lista após cada adicão de um novo nó 
        '''

        # ordena por distância
        sorted_restaurants=distance_sort(restaurants)

        # gera as variáveis auxiliares
        rest_aux=[]
        rest_final=[]
        dist_atual=None

        # ordenando por avaliação do cliente
        for i,r in enumerate(sorted_restaurants):
            
            if not dist_atual:
                dist_atual=r.distance

            
            if i == len(sorted_restaurants)-1 and r.distance == dist_atual:
                rest_aux.append(r)
                rest_aux=customer_rating_sort(rest_aux)
                rest_final+=rest_aux
                rest_aux=[]
            elif i == len(sorted_restaurants)-1: 
                rest_aux=customer_rating_sort(rest_aux)
                rest_aux.append(r)
                rest_final+=rest_aux
                rest_aux=[]
            elif r.distance == dist_atual:
                rest_aux.append(r)
            else:
                rest_aux=customer_rating_sort(rest_aux)
                rest_final+=rest_aux
                rest_aux=[]
                rest_aux.append(r)
                dist_atual=r.distance

        # aramazenando os resultados obtidos
        sorted_restaurants=rest_final

        # resetando as variáveis auxiliares
        rest_final=[]
        rest_aux=[]

        # gerando uma nova variável auxiliar
        rating_atual=None

        # ordenando por preço
        for i,r in enumerate(sorted_restaurants):

            if not rating_atual:
                rating_atual=r.customer_rating

            if i == len(sorted_restaurants)-1 and r.customer_rating == rating_atual:
                rest_aux.append(r)
                rest_aux=price_sort(rest_aux)
                rest_final+=rest_aux
                rest_aux=[] 
            elif i == len(sorted_restaurants)-1:
                rest_aux=price_sort(rest_aux)
                rest_aux.append(r)
                rest_final+=rest_aux
                rest_aux=[] 
            elif r.customer_rating == rating_atual:
                rest_aux.append(r)           
            else:
                rest_aux=price_sort(rest_aux)
                rest_final+=rest_aux
                rest_aux=[]
                rest_aux.append(r)
                rating_atual=r.customer_rating

        # armazenando os resultados obtidos
        sorted_restaurants=rest_final
        

        return sorted_restaurants




if __name__ == '__main__':
    from restaurant_importer import restaurant_importer
    from filters import *

    restaurantes=restaurant_importer()  # importando os restaurantes
    #restaurantes=name_search('Kit',restaurantes)    # filtrando por nome
    #restaurantes=customer_rating_search(2,restaurantes) # filtrando por avaliação
    restaurantes=price_search(30, restaurantes) # filtrando por preço
    restaurantes=distance_search(3,restaurantes) # filtrando por distancia
    #restaurantes=cuisine_id_search('KorEan',restaurantes) # filtrando pelo nome da cousine

    pilha=Results()

    pilha.list_to_result(restaurantes)
    
    pilha.list()