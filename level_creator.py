import json
def main():
    level = dict()
    level['name'] = input('Nombre del nivel: ')
    
    cards = dict()
    level['num_questions'] = int(input('Ingrese el número de preguntas: ')) 
    for card in range(level['num_questions']):
        temp = dict()
        temp['statement'] = input('Ingrese enunciado: ')
        for x in range(4):
            temp[f'answer_{x}'] = input(f'Ingrese respuesta [{x+1}]: ')
        cards[f'question_{card}'] = temp
    level['questions'] = cards

    f = open('data/levels.txt', 'a')
    f.write(json.dumps(level))
    f.write('\n')
    f.close()

if __name__ == '__main__':
    main()
