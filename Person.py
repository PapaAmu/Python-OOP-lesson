class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print("Hello, my name is {}. I am {} years old and I am a {}.".format(self.name, self.age, self.gender))

#this is an instance
personA = Person("Themba", 30, "male")

"""Now I am calling the intro method to display person information"""
personA.introduce()