"""
#
#Part: Python while Loop
#
"""
i = 1
while i:
    print("1 = ", i)
    i+=1 # i = i +1

i = 1
while i < 5:
    birint("i =", i)
    if i == 3:
        break
    i+=1 # i = i + 1

#    i = 1
# while i < 5:
#    birint("i =", i)
#    if i == 3:
#        continue
#    i+=1 # i = i + 1

i = 1
while i < 5:
    print("i = ", i)
    i+=1 # i = i + 1
else:
    print("Game over!")

"""
#
#Part: Python while Loop
#
"""
fruits = ["apple" , "banana" , "coconut"]
for fruit in fruits:
    print("Fruit: ", fruit)

for fruit in fruits:
    print("Fruit: ", fruit)
    if fruit == "banana":
        break
    
 for fruit in fruits:
    if fruit == "banana":
        break
    print("Fruit: ", fruit)

for fruit in fruits:
    if fruit == "banana":
        continue
    print("Fruit: ", fruit)

for x in range(len(fruits)):
    print("Numbar: ", x)

for x in range(5):
    print("Numbar: ", x)
else:
    print("Game Over!")

    adjs = ["rad" , "blue" , "green"]
    fruits = ["apple" , "banana" , "coconut"]
for adj in adjs:
    for fruit in fruits
    print("Fruit: " + adj + " " + fruit) 
