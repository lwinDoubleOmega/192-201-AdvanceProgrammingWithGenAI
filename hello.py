print("Hello, John!")

class student: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 

    def display(self): 
        print("Name:", self.name) 
        if self.age >= 18: 
            print("Age:", "Adult")
        else:
            print("Age:", "Underage")


alex = student("Alex", 20)
alex.display()
