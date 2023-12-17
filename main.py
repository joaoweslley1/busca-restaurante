from restaurant_importer import restaurant_importer
from filters import *
from results import *

print("\nSistema de busca de restaurantes!")
    
restaurants = restaurant_importer()
filters_list = []

name=None
rating=None
distance=None
max_price=None
cuisine_name=None

def print_results(restaurants):
    if not restaurants:
        print("Nenhum restaurante encontrado.")
    else:
        for restaurant in restaurants:
            print(restaurant)
            print("-----")

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
        print("\nFiltros Atuais:")
        for i, filter_command in enumerate(filters_list, start=1):
            print(f"{i}. {filter_command}")
        if not filters_list:
            print("Nenhum filtro aplicado.\n")
            continue
        try:
            filter_to_remove = input("\nDigite o número do filtro que deseja remover, 'T' para remover todos, ou '0' para cancelar: ")
            if filter_to_remove == "0":
                continue
            elif filter_to_remove.upper() == "T":
                filters_list = []
                print("Todos os filtros foram removidos.\n")
            else:
                filter_to_remove = int(filter_to_remove)
                if 1 <= filter_to_remove <= len(filters_list):
                    removed_filter = filters_list.pop(filter_to_remove - 1)
                    print(f"Filtro removido: {removed_filter}\n")
                else:
                    print("Número inválido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Tente novamente.")
    elif option == "1":
        name=input("Digite o nome do restaurante: ")
        restaurants=name_search(name,restaurants)
        filters_list.append(f"name_search('{name}', restaurants)")
    elif option == "2":
        rating=int(input("Digite a avaliação mínima: "))
        restaurants=customer_rating_search(rating,restaurants)
        filters_list.append(f"customer_rating_search({rating}, restaurants)")
    elif option == "3":
        distance=float(input("Digite a distância máxima: "))
        restaurants=distance_search(distance,restaurants)
        filters_list.append(f"distance_search({distance}, restaurants)")
    elif option == "4":
        max_price=float(input("Digite o preço máximo: "))
        restaurants=price_search(max_price,restaurants)
        filters_list.append(f"price_search({max_price}, restaurants)")
    elif option == "5":
        cuisine_name=input("Digite o nome da cozinha: ")
        restaurants=cuisine_id_search(cuisine_name,restaurants)
        filters_list.append(f"cuisine_id_search('{cuisine_name}', restaurants)")
    else:
        print("Opção inválida. Tente novamente.")

results=Results()

results.list_to_result(restaurants)

if not name and not rating and not distance and not max_price and not cuisine_name:
    results.list()
else:
    results.list(False)


print("\nComandos Selecionados:")
for command in filters_list:
        print(command)
        print("\n")