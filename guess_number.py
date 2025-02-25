from random import randint

number = randint(1, 100)
print('Угадайте число от 1 до 100')

while True:
    guest = int(input('ВВедите число: '))

    if guest < number:
        print('Ваше число меньше того, что загадано.')
    elif guest > number:
        print('Ваше число больше того, что загадано.')
    elif guest == number:
        break

print('Отличная интуиция! Вы угадали число :)')  