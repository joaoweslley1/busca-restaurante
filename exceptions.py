class InvalidNameException(Exception):
    '''
    Exceção para nome inválido.
    '''
    def __init__(self,message='Nome inválido para o restaurante, espera-se uma string!'):
        super().__init__(message)

class InvalidCustomerRatingException(Exception):
    '''
    Exceção para erro no customer rating.
    '''
    def __init__(self,message='Customer Rating inválida, espera-se um numeral entre 1 e 5!'):
        super().__init__(message)

class InvalidDistanceException(Exception):
    '''
    Exceção para erro na distancia.
    '''
    def __init__(self,message='Distancia inválida, espera-se um valor numeral entre 1 a 10!'):
        super().__init__(message)

class InvalidPriceException(Exception):
    '''
    Exceção para erro no preço.
    '''
    def __init__(self,message='Preço inválido, espera-se um numeral entre 10 e 50!'):
        super().__init__(message)

class InvalidCuisineException(Exception):
    '''
    Exceção para erro no Cuisine ID.
    '''
    def __init__(self,message='Cuisine ID inválido, espera-se um valor presente no arquivo cuisines.csv'):
        super().__init__(message)

class InvalidObjectTypeException(Exception):
    '''
    Exceção para caso objeto não seja um Restaurante.
    '''
    def __init__(self,message='O objeto precisa ser da classe Restaurant'):
        super().__init__(message)