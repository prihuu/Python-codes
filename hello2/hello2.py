"""class Car:
    def __init__(self, brand, color, mileage = 0, fuel = 100):
        self.brand = brand
        self.color = color
        self.mileage = mileage
        self.fuel = fuel

    def drive(self, distance):
        fuel_needed = distance * 0.5
        if self.fuel >= fuel_needed:
            self.mileage += distance
            self.fuel -= fuel_needed
            print(f"The car drove {distance} km. Remaining fuel: {self.fuel:.2f}%.")
        else:
            max_distance = self.fuel / 0.5
            self.fuel = 0
            print(f"The car ran out of fuel after driving {max_distance:.2f} km.")

        print(f"Driven {distance} km. Total mileage is now {self.mileage} km.")
        print(f"The car your driving is a {self.brand} in the color {self.color}")

    def repaint(self, color2):
        self.color = color2
        print(f"The {self.brand} was repainted with the color {self.color}")

car1 = Car("BMW", "red")
car2 = Car("Mercedes", "blue")

car1.drive(10)
car2.drive(60)

car1.drive(100)
car1.repaint("blue")

car2.drive(200)
car2.repaint("red")

class Dog:
    def __init__(self, name, birth_year, sound= "Woof woof"):
        self.name = name
        self.birth_year = birth_year
        self.sound = sound
    def bark(self, times):
        for i in range(times):
            print(self.name+" barks "+self.sound)
            return


class Hotel:
    def __init__(self):
        self.dogs = []
    def dog_checkin(self, dog):
        self.dogs.append(dog)
        print(dog.name + "dog checkin")
        return
    def dog_checkout(self, dog):
        self.dogs.remove(dog)
        print(dog.name + "dog checkout")
        return
    def greet_dogs(self):
        for dog in self.dogs:
            dog.bark(2)
dog1 = Dog("Dolly", "2022")
dog2 = Dog("Royalty", "2020")
dog3 = Dog("Melvin", "2023")
hotel = Hotel()
hotel.dog_checkin(dog1)
hotel.dog_checkin(dog2)
hotel.dog_checkin(dog3)
hotel.greet_dogs()
hotel.dog_checkout(dog2)
hotel.greet_dogs()


class Student:
    def __init__(self, name, age, gender, birth_year, sound = "Yapa yapa"):
        self.name = name
        self.age = age
        self.gender = gender
        self.birth_year = birth_year
        self.sound = sound
    def talking(self, times):
        for i in range(times):
            print(self.name + " talks "+self.sound)
            return

class Teacher:
    def __init__(self):
        self.students = []
    def student_in_class(self, student):
        self.students.append(student)
        print(f"{student.name} in class")
        return
    def student_not_in_class(self, student):
        self.students.remove(student)
        print(f"Teacher removed {student.name} from class")
        return
    def greet_students(self):
        for student in self.students:
            student.talking(2)
student1 = Student("Princess", "19", "Female", "2006")
student2 = Student("Radin", "19", "Male", "2006")
student3 = Student("Clary", "24", "Female", "2001")
student4 = Student("Tara", "23", "Female", "2002")
student5 = Student("Joshua", "24", "Male", "2001")
teacher = Teacher()

teacher.student_in_class(student1)
teacher.student_in_class(student2)
teacher.student_in_class(student3)
teacher.student_in_class(student4)
teacher.student_in_class(student5)
teacher.greet_students()
teacher.student_not_in_class(student1)
teacher.greet_students()


#Base class
class Animal:
    def __init__(self, name, species, sound = "Meow meow"):
        self.name = name
        self.species = species
        self.sound = sound

    def print_info(self):
        print(f" The name of the animal is {self.name} and the species is a {self.species}")

#Subclasses
class Lion(Animal):
    def __init__(self, name, species, sound = "Roar roar"):
        self.species = species
        self.sound = sound
        super().__init__(name, species, sound)

    def print_info(self):
        super().print_info()

class Elephant(Animal):
    def __init__(self, name, species, sound = "Trööt trööt"):
        self.species = species
        self.sound = sound
        super().__init__(name, species, sound)

    def print_info(self):
        super().print_info()


class Snake(Animal):
    def __init__(self, name, species, sound = "Shh shh"):
        self.species = species
        self.sound = sound
        super().__init__(name, species, sound)

    def print_info(self):
        super().print_info()


#Adding zoo
class Zoo:
    def __init__(self):
        self.animals = []
    def animal_in_zoo(self, animal):
        self.animals.append(animal)
        print(f"{animal.sound} in zoo")
        return
    def print_all(self):
        for a in self.animals:
            a.print_info()

#Main program
ani1 = Animal("Tara", "bird")

lion1 = Lion("Princess", "Mammal")

ele1 = Elephant("Joshua", "Mammal")

sna1 = Snake("Radin", "Reptile")

print("There are four (4) animals in the zoo! ")
zoo = Zoo()
zoo.animal_in_zoo(ani1)
zoo.animal_in_zoo(lion1)
zoo.animal_in_zoo(ele1)
zoo.animal_in_zoo(sna1)

zoo.print_all()



#Python module 9
import random
class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

#creating 10 cars
cars = []
for i in range(1, 11):
    registration_number = (f"ABC-{i}")
    maximum_speed = random.randint(100, 200)
    cars.append(Car(registration_number, maximum_speed))

#race
race_over = False
hours_passed = 0
while not race_over:
    hours_passed += 1

    for car in cars:
        speed_change = random.randint(-10, 15)
        car.accelerate(speed_change)
        car.drive(1)

        if car.travelled_distance >= 10000:
            race_over = True

print(f"Race over, hours passed: {hours_passed} hours!")
for car in cars:
    print(car.registration_number, car.maximum_speed, car.current_speed, round(car.travelled_distance, 1))

#creating new car
#car = Car("ABC-123", 142)

#acceleration
#car.accelerate(30)
#car.accelerate(70)
#car.accelerate(50)

#print(f"Current speed after accelerating: {car.current_speed} km/h")

#drive for 1.5h
#car.drive(1.5)
#print(f"Travelled distance: {car.travelled_distance} km/h")

#emergency brake
#car.accelerate(-200)
#print(f"Final speed after emergency brake: {car.current_speed} km/h")

#print("Car details:")
#print(f"Registration number: {car.registration_number}")
#print(f"Maximum speed: {car.maximum_speed} km/h")
#print(f"Current speed: {car.current_speed} km/h")
#print(f"Travelled distance: {car.travelled_distance} km/h")
"""


#Python module 10
import random
class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hours_passed(self):
        for car in self.cars:
            change = random.randint(-10, 15)
            car.accelerate(change)
            car.drive(1)

    def print_status(self):
        print(f"Race: {self.name}")
        for car in self.cars:
            print(f"{car.registration_number}: speed {car.current_speed} km/h, distance {int(car.travelled_distance)} km/h")

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False


class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current_floor = bottom

    def floor_up(self):
        if self.current_floor < self.top:
            self.current_floor += 1
            print(f"Elevator is at floor: {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom:
            self.current_floor -= 1
            print(f"Elevator is at floor: {self.current_floor}")

    def go_to_floor(self, target):
        while self.current_floor < target:
            self.floor_up()
        while self.current_floor > target:
            self.floor_down()

class Building:
    def __init__(self, bottom, top, num_elevators):
        self.elevators = []
        for i in range(num_elevators):
            self.elevators.append(Elevator(bottom, top))

    def run_elevator(self, elevator_num, floor):
        print(f"Elevator {elevator_num} is now at floor: {floor}")
        elevator = self.elevators[elevator_num - 1]
        elevator.go_to_floor(floor)

    def fire_alarm(self):
        print("Fire alarm, all elevators returning to the first floor!")
        for elevator in self.elevators:
            elevator.go_to_floor(elevator.bottom)

#Main program
cars = []
for i in range(1, 11):
    registration_number = (f"ABC-{i}")
    maximum_speed = random.randint(100, 200)
    cars.append(Car(registration_number, maximum_speed))

race = Race("Grand Demolition Derby", 8000, cars)

hours = 0
while not race.race_finished():
    race.hours_passed()
    hours += 1
    if hours % 10 == 0:
        race.print_status()

print(f"Race finished, hours passed: {hours} hours!")

building = Building(1, 10, 3)
building.run_elevator(1, 5)
building.run_elevator(2, 8)
#elevator = Elevator(1, 10)

#elevator.go_to_floor(5)

#elevator.go_to_floor(1)


