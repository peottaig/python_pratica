from random import choice
from time import sleep
print('\033[32m¨\033[33m-\033[34m_' * 5,'Hangman game' ,'\033[34m_\033[33m-\033[32m¨\033[m' * 5)
sleep(1)
print('')
print('This is a word finding game')
print('The word is random, try guess the word')
print('')
word = ('Banana','Amor' , 'Velho', 'Xbox', 'Bando', 'Abacaxi', 'Neymar', 'Batata', 'Azedo' )


separator = ''
lv = (15, 10, 5)

while True:
    Hits = []
    print('Level 1: 15, Level 2: 10, Level 3: 5')   
    lvR = int(input('Chose one dificult for de game:'))
    dif = lv[lvR-1]
    print('')
    print(f'You have {lv[lvR-1]} attempts')
    miss = 0
    letter = ''
    word = ('Banana','Amor' , 'Velho', 'Xbox', 'Bando', 'Abacaxi', 'Neymar', 'Batata', 'Azedo' )
    guess = choice(word)
    for letter in guess:
        Hits.append('_')

    while True:

        

        index = 0
        for word in Hits:
            print('' ,word, end= ' ')
        answ = str(input('\nGuess a letter:  ')).strip().upper()[0]
        for letter in guess:
            if answ == letter.upper():
                Hits[index] = letter
            
            index += 1

        result = [separator.join(Hits)]
        result = result[0]
        
        if miss == lv[lvR-1]:
            print('You lose')
        elif result == guess:
            break
    print(result)    
    print('\nThe game finish ')
    exitt = input('Do you want paly again?').upper().strip()[0]
    while exitt not in 'YN':
        exitt = input('Do you want paly again????').upper().strip()[0]

    if exitt == 'N':
        break
   

    
