

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    

    def say_hello(self):
        print(f'Hello, my name is {self.name} and i\'m {self.age}!')



if __name__ == '__main__':
    p1 = Person('Esteban',21)
    p1.say_hello()