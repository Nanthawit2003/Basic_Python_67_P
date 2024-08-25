"""
#
#Part: Python Function
#
"""
def myFunction():
    i = 1
    while i <= 5:
        print("Hello World ", i)
        i+=1
myFunction()
myFunction()

# parameter
def myNeme(name):
    print("My name is " + name)
myNeme("Anya")
myNeme("Loid")

def myFullNeme(first_name = "Unknown", last_name = "Forger"):
    print("My name is " + first_name + " " +last_name)
myFullNeme("Anya")
myFullNeme("Bond", "Forger")
myFullNeme("Yor", "Forger")
myFullNeme(last_name = "Forger", first_name="Loid")

def myFruit(fruits):
    for fruit in fruits:
        print(fruit)
fruits = ["Apple", "Banana", "Coconut"]
myFruit(fruits)

def redPotion(hp):
    return hp + 50
print("Hp: ", redPotion(100))
print("Hp: ", redPotion(30))

