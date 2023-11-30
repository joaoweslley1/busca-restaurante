from cuisine_importer import cuisine_importer
from exceptions import *

class Restaurant():
    '''
    Classe que instancia os restaurantes.
    '''
    def __init__(self,name=None,customer_rating=None,distance=None,price=None,cuisine_id=None):
        self.name=name
        self.customer_rating=customer_rating
        self.distance=distance
        self.price=price
        self.cuisine_id=cuisine_id
    
    def __str__(self):
        return f'''
    Name: {self.__name}
    Customer Rating: {self.__customer_rating}
    Distance: {self.__distance}
    Price: {self.__price}
    Cuisine ID: {self.__cuisine_id}
    '''

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,n):
        if not isinstance(n,str): raise InvalidNameException()
        self.__name=n

    @property
    def customer_rating(self):
        return self.__customer_rating
    
    @customer_rating.setter
    def customer_rating(self,c):
        if not isinstance(c,(int,float)) or not (1 <= c <= 5): raise InvalidCustomerRatingException()
        self.__customer_rating=c

    @property
    def distance(self):
        return self.__distance
    
    @distance.setter
    def distance(self,d):
        if not isinstance(d,(int,float)) or not (1 <= d <= 10): raise InvalidDistanceException() 
        self.__distance=d
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self,p):
        if not isinstance(p,(int,float)) or not (10 <= p <= 50): raise InvalidPriceException() 
        self.__price=p
    
    @property
    def cuisine_id(self):
        return self.__cuisine_id
    
    @cuisine_id.setter
    def cuisine_id(self,c):
        cuisines=cuisine_importer('./csv_files/cuisines.csv')
        if c not in cuisines[0]: raise InvalidCuisineException()
        self.__cuisine_id=c


if __name__ == '__main__':
    restaurant=Restaurant('Restaurante Teste',5,5,10,6)
    print(restaurant)