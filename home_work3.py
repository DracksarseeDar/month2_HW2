class Person:
    def __init__(self, name, birth_date, occupation , higher_education):
        self.name = name
        self.birth_date = birth_date
        self.__occupation = occupation
        self.__higher_education = higher_education

    @property
    def occupation(self):
        return self.__occupation
    @property
    def higher_education(self):
        return self.__higher_education

    def introduce(self):
        edu = 'есть высшее образование' if self.higher_education else 'нет высшего образования'
        print(f'Привет меня зовут {self.name} , я родился  {self.birth_date} , я  {self.occupation} , у меня {edu}')

class Classmate(Person):
    def __init__(self , name , birth_date , occupation , group , higher_education):
        super().__init__(name , birth_date , occupation , higher_education)
        self.group = group

    def introduce(self):
        edu = 'есть высшее образование' if self.higher_education else 'нет высшего образования'
        print(f'Привет! я из класса {self.group} , меня зовут {self.name} , я родился  {self.birth_date} , я {self.occupation}, у меня {edu}')

class Friend(Person):
    def __init__(self , name , birth_date , occupation , hobby , higher_education):
        super().__init__(name , birth_date , occupation , higher_education)
        self.hobby = hobby

    def introduce(self):
        edu = 'есть высшее образование' if self.higher_education else 'нет высшего образования'
        print(f'Привет меня зовут {self.name} , я родился  {self.birth_date} , я  {self.occupation} , мое хобби {self.hobby} , у меня {edu}')


classmate1 = Classmate('Адам' ,'14.12.2008' ,'Ученик' ,'11-Д'  , False )
classmate2 = Classmate('Бэйн' ,'01.03.2008' ,'Ученик' ,'11-Б' , False )

friend1 = Friend('Андрей' ,'16.11.2007' ,'Студент' ,'Играть в МК и Valorant', False )
friend2 = Friend('Айдин' ,'07.07.2007' ,'Студент' ,'Изучает сварку и пайку' , False )


classmate1.introduce()
classmate2.introduce()
print()
friend1.introduce()
friend2.introduce()