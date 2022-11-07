# задача 1. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# Делаем игру против бота
# Подумайте как наделить бота ""интеллектом""

# k всего конфет -2021
# m можно максимально взять за ход - 28
# n - количество ходов при коором гарантированно побеждает 

from random import randint

def comp_step(amount, max_step):
    if amount >= max_step: 
        comp_step = randint(1, max_step)
        print(f'Компьютер взял {comp_step}')
        return comp_step
    else: 
        comp_step = randint(1, amount)
        print(f'Компьютер взял {comp_step}')
        return comp_step

def clever_comp_step(amount, max_step):
    comp_step = amount % (max_step + 1)
    if comp_step == 0:
        if amount >= max_step: 
            comp_step = randint(1, max_step)
        else:
            comp_step = randint(1, amount)
    print(f'Компьютер взял {comp_step}')        
    return comp_step

def check_user_step(amount, max_step, player):
    step = int(input(f'{player}, сколько будете брать конфет? '))
    if amount >= max_step:
        while step < 1 or step > max_step:
            step = int(input(f'Можно брать от 1 до {max_step} конфет, сколько берем? '))     
    else:
        while step < 1 or step > amount:
            step = int(input(f'На столе уже нет столько конфет. Можно брать от 1 до {amount}, {player} сколько берем? '))
    return step

def game_pvp (amount, max_step):
    player_1 = input('Введите имя первого игрока: ')
    player_2 = input('Введите имя второго игрока: ')
    print('Сейчас монетка определит кто будет ходить первым, кидаем... и это будет', end='... ')
    choise = randint(0,2)
    if choise:
        print(f' {player_1}')
    else:
        print(f' {player_2}')
    print(f'Напоминаю, что всего конфет на столе {amount}, берем по очереди от 1 до {max_step} или забираем все что осталось')
    while amount > 0:
        if choise:
            amount -= check_user_step(amount, max_step, player_1)
            choise = False
            if amount == 0:
                print(f'Победитель - {player_1}. Поздравляю!!!')
            else:
                print(f'Осталось {amount}')
        else:
            amount -= check_user_step(amount, max_step, player_2)
            choise = True
            if amount == 0:
                print(f'Победитель - {player_2}. Поздравляю!!!')
            else:
                print(f'Осталось {amount}')

def game_comp_person(amount, max_step):
    player_1 = input('Как вас зовут? ')
    print(f'Напоминаю, что всего конфет на столе {amount}, берем по очереди от 1 до {max_step} или забираем все что осталось')  
    print('Разыграем, кто ходит первый и это будет ....', end=' ')
    choise = randint(1,2)
    if choise == 1:
        print(f'{player_1}')
    else:
        print('Компьютер')
    while amount > 0:
        if choise %2 != 0:
            amount -= check_user_step(amount, max_step, player_1)
            if amount == 0:
                print(f'{player_1}, Вы выиграли, поздравляю!!!')
            else:
                print(f'Осталось {amount}')
        else:
            amount -= comp_step(amount, max_step)
            if amount == 0:
                print(f'Выиграл Компьютер, хоть он и не очень умный')
            else:
                print(f'Осталось {amount}')
        choise +=1

def game_clever_comp_person(amount, max_step):
    player_1 = input('Как вас зовут? ')
    print(f'Напоминаю, что всего конфет на столе {amount}, берем по очереди от 1 до {max_step} или забираем все что осталось')  
    print('Разыграем, кто ходит первый и это будет ....', end=' ')
    choise = randint(1,2)
    if choise == 1:
        print(f'{player_1}')
    else:
        print('Компьютер')
    while amount > 0:
        if choise %2 != 0:
            amount -= check_user_step(amount, max_step, player_1)
            if amount == 0:
                print(f'{player_1}, Вы выиграли, поздравляю!!!')
            else:
                print(f'Осталось {amount}')
        else:
            amount -= clever_comp_step(amount, max_step)
            if amount == 0:
                print(f'Выиграл Компьютер')
            else:
                print(f'Осталось {amount}')
        choise +=1

print('Начнем :)')
amount = int(input('Сколько конфет на столе? '))
max_step = int(input('А по сколько максимум будут брать игроки? '))
# game_pvp (amount, max_step)
# game_comp_person(amount, max_step)
game_clever_comp_person(amount, max_step)

