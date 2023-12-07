from cuisine_importer import cuisine_importer
from restaurant_importer import restaurant_importer

# Constante com a lista de restaurantes
RESTAURANTS=restaurant_importer()


def name_search(restaurant_name:str,restaurants:list=RESTAURANTS):
    '''
    Função de busca por nome do restaurante.
    Retorna os restaurantes que possuem suas iniciais iguais a passada.
    '''

    name_length=len(restaurant_name) # pega o tamanho do nome passado

    # filtra os restaurantes, observando se as iniciais são iguais as passadas
    filtered_restaurants=[r for r in restaurants if str(r.name[:name_length]).upper()==restaurant_name.upper()] 

    return filtered_restaurants



def customer_rating_search(minimal_customer_rating:int,restaurants:list=RESTAURANTS):
    '''
    Função de busca por avaliação do cliente do restaurante.
    Retorna apenas os restaurantes que possuem uma avaliação maior ou igual a passada.
    '''

    # filtra os restaurantes levando em consideração a avaliação
    filtered_restaurants=[r for r in restaurants if r.customer_rating >= minimal_customer_rating]

    return filtered_restaurants



def distance_search(max_distance:float,restaurants:list=RESTAURANTS):
    '''
    Função de busca por distancia até o restaurante.
    Retorna apenas os restaurantes que possuem uma distância menor ou igual a passada.
    '''

    # filtra os restaurantes levando em consideração a distancia
    filtered_restaurants=[r for r in restaurants if r.distance <= max_distance]

    return filtered_restaurants



def price_search(max_price:float,restaurants:list=RESTAURANTS):
    '''
    Função de busca por preço médio do restaurante.
    Retorna apenas os restaurantes que possuem uma preço menor ou igual ao passado.
    '''

    # filtra os restaurantes levando em consideração o preço
    filtered_restaurants=[r for r in restaurants if r.price <= max_price]

    return filtered_restaurants



def cuisine_id_search(cuisine_name:str,restaurants:list=RESTAURANTS):
    '''
    Função de busca por nome da cuisine.
    Retorna apenas os restaurantes que suas cuisines iniciem com as iniciais do filtro passado.
    '''

    # pega o tamanho do nome passado
    name_length=len(cuisine_name)

    # importa as cuisines
    cuisines=cuisine_importer()

    #armazena o id da cuisine que corresponde com o nome (ou o trecho do nome) passado
    cuisine_id=[int(c['cuisine_id']) for c in cuisines[1] if str(c['cuisine_name'][:name_length]).upper()==cuisine_name.upper()][0]

    #armazena os restaurantes que possuem o id da cuisine
    filtered_restaurants=[r for r in restaurants if r.cuisine_id == cuisine_id]

    return filtered_restaurants

if __name__ == '__main__':

    restaurantes=restaurant_importer()

    # teste do filtro da customer_rating
    restaurantes_filtrados=customer_rating_search(2,restaurantes)

    # teste do filtro de distancia
    restaurantes_filtrados=distance_search(3,restaurantes_filtrados)

    # teste do filtro do preço
    restaurantes_filtrados=price_search(20,restaurantes_filtrados)

    # teste do filtro da cuisine id
    restaurantes_filtrados=cuisine_id_search('AME',restaurantes_filtrados)

    # teste do filtro de name
    restaurantes_filtrados=name_search('kit',restaurantes_filtrados)

    print(''.join([r.__str__() for r in restaurantes_filtrados]))