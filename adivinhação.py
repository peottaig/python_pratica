from random import randint

def jogar():
    print('\033[34m-=' * 20, '\033[m')

    print('Guessing game')

    print('\033[34m-=' * 20, '\033[m')

    print('A number will be chosen at random')
    print('According to the selected level, it will be more difficult to hit the number and there will be fewer attempts.')

    print('\033[34m-=' * 20, '\033[m')

    lv1 = (10, 1, 100)
    lv2 = (8, 1, 1000)
    lv3 = (4, 1, 1500)
    lv4 = (3, 1, 2000)
    lv5 = (5, 1, 10000)

    win = lose = 0
    while True:
        level = int(input('Choose one level [1, 2, 3, 4, 5]: '))
        while level not in (1, 2, 3, 4, 5):
            level = int(input('Invalid choose [1, 2, 3, 4, 5]: '))

        if level == 1:
            level = lv1

        elif level == 2:
            level = lv2

        elif level == 3:
            level = lv3

        elif level == 4:
            level = lv4

        else:
            level = lv5
        
        cont = 1
        guess = randint(level[1], level[2])
        trY = 0
        
        print(f'The number is between {level[1]} and {level[2]}')

        while cont != level[0]:
            trY = int(input(f'Attempt {cont} of {level[0]}: '))
            if trY == guess:
                print('Congratulations, you guessed the number')
                
                break
            if cont == 1:
                bigger = small = trY
            cont += 1 
            if trY > guess:
                print('Less')

            elif trY < guess:
                print('Bigger')
        if trY != guess:
            print('You lose the game')
            lose += 1

        exiT = input(str('Do you play again?: ')).strip().upper()[0]
        while exiT not in 'SN': 
            exiT = input(str('Do you play again?: ')).strip().upper()[0]
        if exiT == 'N':
            print('Thanks for you colaboration')
            break

if (__name__ == "__main__"):
    jogar()