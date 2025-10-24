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
"""

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
