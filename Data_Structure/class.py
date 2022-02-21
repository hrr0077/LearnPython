class Person:
    def __init__(self, name):
        self.name = name
    
    def say_hi(self):
        print("Hello, My Name is ",self.name)


p = Person('Ritik')
p.say_hi()
