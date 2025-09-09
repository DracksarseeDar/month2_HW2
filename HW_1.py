class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        edu = 'есть высшее образование' if self.higher_education else 'нет высшего образования'
        print(f'Привет! Меня зовут {self.name}. '
              f'Я родился {self.birth_date}, моя профессия — {self.occupation}. '
              f'У меня {edu}.')

# Создаем несколько экземпляров
person1 = Person('Иванов Иван', '12.05.1998', 'Инженер', True)
person2 = Person('Асаналиев Айдин', '07.07.2007', 'Студент', False)
person3 = Person('Хацунэ Мику', '31.08.2007', 'Айдол', False)

# Распечатываем атрибуты
print(person1.name, person1.birth_date, person1.occupation, person1.higher_education)
print(person2.name, person2.birth_date, person2.occupation, person2.higher_education)
print(person3.name, person3.birth_date, person3.occupation, person3.higher_education)

person1.introduce()
person2.introduce()
person3.introduce()



