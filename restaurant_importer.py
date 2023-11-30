import csv
from restaurant import Restaurant

def restaurant_importer(path:str):
    '''
    Função que importa os restaurantes de um arquivo csv.
    O arquivo precisa está no formato: "name,customer_rating,distance,price,cuisine_id"
    '''
    restaurants = []
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader, None)  # pula os cabeçalhos
        for row in csv_reader:
            restaurant = Restaurant(row[0],int(row[1]),int(row[2]),int(row[3]),int(row[4]))
            restaurants.append(restaurant)
    
    return restaurants