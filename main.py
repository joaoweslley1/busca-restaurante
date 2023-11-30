from restaurant_importer import restaurant_importer

caminho='./csv_files/restaurants.csv'
restaurantes=restaurant_importer(caminho)
print(''.join([r.__str__() for r in restaurantes]))