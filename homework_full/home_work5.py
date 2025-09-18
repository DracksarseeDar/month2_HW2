from homework_full.distance import Distance

if __name__ == '__main__':
    distance1 = Distance( 100 , 'm')
    distance2 = Distance(2 , 'km')
    distance3 = Distance(100000 , 'mm')

    print('Инициализация')
    print(distance1)
    print(distance2)
    print(distance3)

    print('Сложение')
    print(distance1 + distance2)
    print(distance1 + distance3)
    print(distance2 + distance3)

    print('Вычитание')
    print(distance1 - distance3)
    print(distance2 - distance3)
    try:
        print(distance1 - distance2)
    except ValueError:
        print('ошибка')

    print('Сравнение')
    print(distance2 == Distance(2000 , 'm'))
    print(distance2 == Distance(190000, 'cm'))




















