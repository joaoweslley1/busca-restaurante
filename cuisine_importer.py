import csv

def cuisine_importer(path:str=None):
    '''
    Função que importa as cuisines de um arquivo csv.
    Permite que um caminho seja passado.
    '''

    if not path:
        path='./csv_files/cuisines.csv' # caminho padrão

    cuisines=[]
    cuisines_id=[]
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader, None)  # pula os cabeçalhos
        for row in csv_reader:
            cuisine = dict()
            cuisine['cuisine_id']=row[0]
            cuisine['cuisine_name']=row[1]
            cuisines.append(cuisine)
            cuisines_id.append(int(row[0]))

    return [cuisines_id,cuisines]
