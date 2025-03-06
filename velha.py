from random import choice
from time import sleep

def jogar():
    
    print('   \033[32mX\033[m|O |O')
    print('   O|\033[32mX\033[m |X  \033[34mWelcome to hash game by text\033[m')
    print('   O|O |\033[32mX\033[m')

    skinU = str(input('Select X or O: ')).strip().upper()[0]
    skinB = ''
    select = 0
    while skinU not in 'XO':
        skinU = str(input('Please select a valid answer: ')).strip().upper()[0]

    print('-=' * 20)
    if skinU in 'X':
        skinB = 'O'
    elif skinU in 'O':
        skinB = 'X'
    print(f'User = [{skinU}]||| Bot = [{skinB}]')
    print('-=' * 20)
    exitt = True
    while exitt:
        spots = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        game = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        regU = []
        regB = []
        yn = ''
        while True:
            print(game[0],'|',game[1],'|',game[2])    
            print(game[3],'|',game[4],'|',game[5]) 
            print(game[6],'|',game[7],'|',game[8]) 

            
            
            while True:
                select = int(input('Choose a position that is not occupied: '))
                if select in spots:
                    regU.append(select)
                    break 

            for index, value in enumerate(game):
                if value == select:
                    game[index] = skinU

            sleep(1)
            print(f'You played in position {select}')
            sleep(1)
            print(game[0],'|',game[1],'|',game[2])    
            print(game[3],'|',game[4],'|',game[5]) 
            print(game[6],'|',game[7],'|',game[8]) 
            sleep(2)

            if 1 in regU:
                if 2 in regU:
                    if 3 in regU:
                        print('\033[33mcongratulations, you win')
                        break

            if 2 in regU:
                if 5 in regU:
                    if 8 in regU:
                        print('\033[33mcongratulations, you win')
                        break
            
            if 4 in regU:
                if 5 in regU:
                    if 6 in regU:
                        print('\033[33mcongratulations, you win')
                        break

            if 1 in regU:
                if 4 in regU:
                    if 7 in regU:
                        print('\033[33mcongratulations, you win')
                        break    

            if 7 in regU:
                if 8 in regU:
                    if 9 in regU:
                        print('\033[33mcongratulations, you win')
                        break
            
            if 3 in regU:
                if 6 in regU:
                    if 9 in regU:
                        print('\033[33mcongratulations, you win')
                        break

            if 1 in regU:
                if 5 in regU:
                    if 9 in regU:
                        print('\033[33mcongratulations, you win')
                        break    

            if 3 in regU:
                if 5 in regU:
                    if 7 in regU:
                        print('\033[33mcongratulations, you win')
                        break     
            

            spots.remove(select)  
            bot = choice(spots) 
            regB.append(bot)
            spots.remove(bot)

            print('bots turn')
            sleep(1)
            for index, value in enumerate(game):
                if value == bot:
                    game[index] = skinB
            print(f'bot played in position {bot}')
            sleep(2)

            if 1 in regB:
                if 2 in regB:
                    if 3 in regB:
                        print('\033[33mHow sad you lost')
                        break

            if 2 in regB:
                if 5 in regB:
                    if 8 in regB:
                        print('\033[33mHow sad you lost')
                        break
                
            if 4 in regB:
                if 5 in regB:
                    if 6 in regB:
                        print('\033[33mHow sad you lost')
                        break

            if 1 in regB:
                if 4 in regB:
                    if 7 in regB:
                        print('\033[33mHow sad you lost')
                        break    

            if 7 in regB:
                if 8 in regB:
                    if 9 in regB:
                        print('\033[33mHow sad you lost')
                        break
            
            if 3 in regB:
                if 6 in regB:
                    if 9 in regB:
                        print('\033[33mHow sad you lost')
                        break

            if 1 in regB:
                if 5 in regB:
                    if 9 in regB:
                        print('\033[33mHow sad you lost')
                        break    

            if 3 in regB:
                if 5 in regB:
                    if 7 in regB:
                        print('\033[33mHow sad you lost')
                        break     
            
            
        yn = str(input('Do you want to continue playing?: ')).strip().upper()[0]
        while yn not in 'SN':
            yn = str(input('Please, put a valid answer')).strip().upper()[0]
        if yn == 'N':
            break
    print('The game finish, thanks for play\033[m')

if (__name__ == "__main__"):
    jogar()