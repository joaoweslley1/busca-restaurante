def name_sort(restaurants:list):
    '''
    Mecanismo de orednação baseado no nome do restaurante;
    Utiliza o método quicksort, utilizando como pivô o primeiro elemento da lista
    e em seguida realiza a ordenação baseada na propriedade name do restaurante. 
    '''

    if len(restaurants) <= 1: return restaurants
    pivo = restaurants[0]
    iguais = [r for r in restaurants if r.name == pivo.name]
    menores = [r for r in restaurants if r.name < pivo.name]
    maiores = [r for r in restaurants if r.name > pivo.name]
    return name_sort(menores) + iguais + name_sort(maiores)

def customer_rating_sort(restaurants:list):
    '''
    Mecanismo de orednação baseado na avaliação dos clientes do restaurante;
    Utiliza o método quicksort, utilizando como pivô o primeiro elemento da lista
    e em seguida realiza a ordenação baseada na propriedade customer_rating do restaurante. 
    '''

    if len(restaurants) <= 1: return restaurants
    pivo = restaurants[0]
    iguais = [r for r in restaurants if r.customer_rating == pivo.customer_rating]
    menores = [r for r in restaurants if r.customer_rating < pivo.customer_rating]
    maiores = [r for r in restaurants if r.customer_rating > pivo.customer_rating]
    return customer_rating_sort(maiores) + iguais + customer_rating_sort(menores)


def distance_sort(restaurants:list):
    '''
    Mecanismo de orednação baseado na distância até o restaurante;
    Utiliza o método quicksort, utilizando como pivô o primeiro elemento da lista
    e em seguida realiza a ordenação baseada na propriedade distance do restaurante. 
    '''
    if len(restaurants) <= 1: return restaurants
    pivo = restaurants[0]
    iguais = [r for r in restaurants if r.distance == pivo.distance]
    menores = [r for r in restaurants if r.distance < pivo.distance]
    maiores = [r for r in restaurants if r.distance > pivo.distance]
    return distance_sort(menores) + iguais + distance_sort(maiores)


def price_sort(restaurants:list):
    '''
    Mecanismo de orednação baseado no preço médio do restaurante;
    Utiliza o método quicksort, utilizando como pivô o primeiro elemento da lista
    e em seguida realiza a ordenação baseada na propriedade price do restaurante. 
    '''

    if len(restaurants) <= 1: return restaurants
    pivo = restaurants[0]
    iguais = [r for r in restaurants if r.price == pivo.price]
    menores = [r for r in restaurants if r.price < pivo.price]
    maiores = [r for r in restaurants if r.price > pivo.price]
    return price_sort(menores) + iguais + price_sort(maiores)