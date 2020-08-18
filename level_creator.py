import json
def main():
    level = dict()
    level['name'] = input('Nombre del nivel: ')
    
    cards = dict()
    level['num_cards'] = int(input('Ingrese número de cartas: ')) 
    for card in range(level['num_cards']):
        temp = dict()
        temp['statement'] = input('Ingrese enunciado: ')
        for x in range(4):
            temp[x] = input(f'Ingrese respuesta [{x}]: ')
        cards[card] = temp
    level['cards'] = cards

    f = open('data/levels.txt', 'a')
    f.write(json.dumps(level))
    f.write('\n')
    f.close()

if __name__ == '__main__':
    main()
