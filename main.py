from restaurant_importer import restaurant_importer
from restaurant import *
from filters import *
from cuisine_importer import *
caminho='./csv_files/restaurants.csv'
restaurantes=restaurant_importer(caminho)


def print_restaurants(restaurants):
    if not restaurants:
        print("Nenhum restaurante encontrado.")
    else:
        for restaurant in restaurants:
            print(restaurant)
            print("-----")

def main():
    print("\nSistema de busca de restaurantes!")
    
    RESTAURANTS = restaurant_importer()
    
    selected_filters = []

    while True:
        print("\nEscolha uma opção:")
        print("1. Buscar por nome do restaurante")
        print("2. Buscar por avaliação do cliente")
        print("3. Buscar por distância")
        print("4. Buscar por preço médio")
        print("5. Buscar por tipo de cozinha")
        print("0. Pesquisar")

        option = input("Opção: ")

        if option == "0":
            break
        elif option == "1":
            restaurant_name = input("Digite o nome do restaurante: ")
            selected_filters.append(lambda restaurants: name_search(restaurant_name, restaurants))
        elif option == "2":
            rating = int(input("Digite a avaliação mínima: "))
            selected_filters.append(lambda restaurants: customer_rating_search(rating, restaurants))
        elif option == "3":
            distance = float(input("Digite a distância máxima: "))
            selected_filters.append(lambda restaurants: distance_search(distance, restaurants))
        elif option == "4":
            max_price = float(input("Digite o preço máximo: "))
            selected_filters.append(lambda restaurants: price_search(max_price, restaurants))
        elif option == "5":
            cuisine_name = input("Digite o nome da cozinha: ")
            selected_filters.append(lambda restaurants: cuisine_id_search(cuisine_name, restaurants))
        else:
            print("Opção inválida. Tente novamente.")

    
    filtered_restaurants = RESTAURANTS
    for selected_filter in selected_filters:
        filtered_restaurants = selected_filter(filtered_restaurants)

    print("\nResultados da busca:")
    print_restaurants(filtered_restaurants)


if __name__ == "__main__":
    main()
