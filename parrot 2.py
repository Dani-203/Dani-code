class Parrot:

    # intance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def sing(self, song):
        return "{} is now dancing".format(self.name)
    
# instantiate the object
blu = Parrot("Blu", 10)

# call our instanse metods
print(blu.sing("'Happy'"))