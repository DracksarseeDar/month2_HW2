#
#self
class Car:
    def __init__(self , color , model):
        self.color = color
        self.model = model

    def drive_to_location(self , location):
        print(f'car {self.model}  driving to {location}')



car_honda = Car(color='red',model='Honda')
print(car_honda.color)
print(car_honda)
print(f'color {car_honda.color} , model {car_honda.model}')

car_honda.color = 'blue'
print(f'color {car_honda.color} , model {car_honda.model}')

car_subaru = Car(color='black',model='Subaru')
car_subaru.drive_to_location('Osh')

print(car_subaru)
print(type(12334556))
print(type('hello world'))
print(int( 1324+4534 ))































