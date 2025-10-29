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
"""

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