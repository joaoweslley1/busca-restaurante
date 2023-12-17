from restaurant_importer import restaurant_importer
from filters import *
from results import *

print("\nSistema de busca de restaurantes!")
    
restaurants = restaurant_importer()

name=None
rating=None
distance=None
max_price=None
cuisine_name=None

while True:
    print("======================================")
    print("          Escolha uma opção:          ")
    print("======================================")
    print("[1] Buscar por nome do restaurante")
    print("[2] Buscar por avaliação do cliente")
    print("[3] Buscar por distância")
    print("[4] Buscar por preço médio")
    print("[5] Buscar por tipo de cozinha")
    print("[R] Resetar")
    print("[P] Pesquisar")
    print("======================================")

    option = input("\n\nOpção: ")

    if option.upper() == "P":
        if not name and not rating and not distance and not max_price and not cuisine_name:
            break
        else:
            print("Filtros Selecionados:\n")
            if name:
                print('Nome: ',name)
            if rating:
                print('Rating: ', rating)
            if distance:
                print('Distãncia máxima: ', distance)
            if max_price:
                print('Preço máximo: ',max_price)
            if cuisine_name:
                print('Nome da cuisine: ', cuisine_name)
            print('')
            print('Realizar pesquisa? [S/n]')
            option=input()
            if option == '' or option.upper() == 'S':
                break
            elif option.upper() == 'N':
                continue
            else:
                print('Opção inválida!')
    elif option.upper() == "R":
        restaurants=restaurant_importer()
    elif option == "1":
        name=input("Digite o nome do restaurante: ")
        restaurants=name_search(name,restaurants)
    elif option == "2":
        rating=int(input("Digite a avaliação mínima: "))
        restaurants=customer_rating_search(rating,restaurants)
    elif option == "3":
        distance=float(input("Digite a distância máxima: "))
        restaurants=distance_search(distance,restaurants)
    elif option == "4":
        max_price=float(input("Digite o preço máximo: "))
        restaurants=price_search(max_price,restaurants)
    elif option == "5":
        cuisine_name=input("Digite o nome da cozinha: ")
        restaurants=cuisine_id_search(cuisine_name,restaurants)
    else:
        print("Opção inválida. Tente novamente.")

results=Results()

results.list_to_result(restaurants)

if not name and not rating and not distance and not max_price and not cuisine_name:
    results.list()
else:
    results.list(False)
