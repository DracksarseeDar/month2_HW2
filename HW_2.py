class Person:
    def __init__(self, name, birth_date, occupation):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation

    def introduce(self):
        print(f'Привет меня зовут {self.name} , я родился  {self.birth_date} , я  {self.occupation}')

class Classmate(Person):
    def __init__(self , name , birth_date , occupation , group):
        super().__init__(name , birth_date , occupation)
        self.group = group

    def introduce(self):
        print(f'Привет! я из класса {self.group} , меня зовут {self.name} , я родился  {self.birth_date} , я {self.occupation}')

class Friend(Person):
    def __init__(self , name , birth_date , occupation , hobby):
        super().__init__(name , birth_date , occupation)
        self.hobby = hobby

    def introduce(self):
        print(f'Привет меня зовут {self.name} , я родился  {self.birth_date} , я  {self.occupation} , мое хобби {self.hobby}')

# person1 = Person(' ' , '' ,'')

classmate1 = Classmate('Адам' ,'14.12.2008' ,'Ученик' ,'11-Д' )
classmate2 = Classmate('Бэйн' ,'01.03.2008' ,'Ученик' ,'11-Б' )

friend1 = Friend('Андрей' ,'16.11.2007' ,'Студент' ,'Играть в МК и Valorant' )
friend2 = Friend('Айдин' ,'07.07.2007' ,'Студент' ,'Изучает сварку и пайку' )


classmate1.introduce()
classmate2.introduce()
print()
friend1.introduce()
friend2.introduce()