class Dog:
    species = "Canine"  # Class attribute
    state = "Alive"

    def __init__(self, name, age, color):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute
        self.color = color

dog1 = Dog("Buddy", 3, "Black")  # Create an instance of Dog
dog2 = Dog("Charlie", 5, "Grey")  # Create another instance of Dog

print(dog1.name, dog1.age, dog1.species, dog1.state)  # Access instance and class attributes
print(dog2.name, dog2.age, dog2.species, dog2.color)  # Access instance and class attributes
print(Dog.species)  # Access class attribute directly
print(Dog.state)

Dog.state = "Dead"

print(dog1.state)