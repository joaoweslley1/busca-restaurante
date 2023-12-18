# Busca Restaurante

Projeto final da disciplina de Programação e Estrutura de Dados do curso Redes de Computadores, período 2023.2.

## Índice

- [Visão Geral](#visão-geral)
- [Requisitos e Dependências](#requisitos-e-dependências)
- [Instruções de Instalação](#instruções-de-instalação)
- [Como Executar o Projeto](#como-executar-o-projeto)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Funcionalidades Principais](#funcionalidades-principais)
- [Gestão de Erros e Exceções](#gestão-de-erros-e-exceções)

## Visão Geral

O projeto Busca Restaurante é uma aplicação que tem por objetivo buscar, filtrar e ordernar dados coletados de uma base dados de restaurantes e assim listá-lo baseado em filtros passados pelo usuário. Ele foi desenvolvido como projeto final da disciplina de Programação e Estrutura de Dados do curso Redes de Computadores, período 2023.2.

## Requisitos e Dependências

- Python (versão 3.10.12)

## Instruções de Instalação

1. Clone o repositório: `git clone https://github.com/joaoweslley1/busca-restaurante.git`
2. Navegue até o diretório do projeto: `cd busca-restaurante`

## Como Executar o Projeto

1. Execute o aplicativo: `python main.py`

## Estrutura do Projeto


- `/busca-restaurante`: DIretório principal que armazena tudo.
    - `/csv_files`: Arquivos csv com os dados.
    - `main.py`: Ponto de entrada da aplicação.

## Funcionalidades Principais

### Ordenação de objetos

Ordena os restaurantes contidos em uma lista baseado em um dos seguintes critérios: restaurante, avaliação do cliente, distância e preço.

```python

from restaurant_importer import restaurant_importer

restaurantes=restaurant_importer()                          # importando os restaurantes
restaurante_ordenados1=name_sort(restaurantes)              # ordenado por nome
restaurante_ordenados2=customer_rating_sort(restaurantes)   # ordenado por avaliação do cliente
restaurante_ordenados3=distance_sort(restaurantes)          # ordenado por distância
restaurante_ordenados4=price_sort(restaurantes)             # ordenado por preço
```

### Filtragem de resultados

Filtrar restaurantes por cinco filtros possíveis: nome do restaurante, avaliação do cliente, distância, preço e nome da cousine.

```python
# Exemplo de uso
from restaurant_importer import restaurant_importer
from filters import *

restaurantes=restaurant_importer()  # importando os restaurantes
restaurantes=name_search('Kit',restaurantes)    # filtrando por nome
restaurantes=customer_rating_search(2,restaurantes) # filtrando por avaliação
restaurantes=price_search(30, restaurantes) # filtrando por preço
restaurantes=distance_search(3,restaurantes) # filtrando por distancia
restaurantes=cuisine_id_search('America',restaurantes) # filtrando pelo nome da cousine

pilha=Results()

pilha.list_to_result(restaurantes)
    
pilha.list(False)
```

## Gestão de erros e excessões

O projeto utiliza uma abordagem robusta para lidar com erros e exceções. Mensagens de erro significativas são geradas para facilitar a identificação e solução de problemas. Com foco principal na importação dos dados.