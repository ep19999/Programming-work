#4-1 Pizzas
pizza = ["margerita", "pepperoni", "meat feast"]
for n in pizza:
    print(n)

#4-2 Animals
animals = ["Dog", "Cat", "Frog"]
for a in animals:
    print("A " + a + " would make a great pet")
print("These animals all have autism")

#4-3 Counting to 20
for n in range(1, 21):
    print(n)

#4-4 One Million
num_list = range(1, 1000001)

#4-5 Summing a Million
print(min(num_list))
print(max(num_list))

#4-6 Odd Numbers
odd_list = range(1, 21, 2)
for n in odd_list:
    print(n)

#4-7 Threes
threes_list = range(3,31,3)
for n in threes_list:
    print(n)

#4-8 Cubes 
cubes=[]
for n in range(1,11):
    cubes.append(n**3)
print(cubes)

#4-9 Cube Comprehension
cubes = [n**3 for n in range(1,11)]
print(cubes)

#4-10 Slices
threes_list = range(3,31,3)
print("The first three items in the list are: ")
for n in threes_list[:3]:
    print(n)
    
print("The three items in the middle are")
for n in threes_list[len(a)]:
    print(n)

print("The last three items from the list are: ")
for n in threes_list[-3:]:
    print(n)

# 4-11 Pizza
friend_pizzas = pizza
pizza.append("Ham & Pineapple")
friend_pizzas.append("American Hot")
print("My favourite pizzas are: \n")
for p in pizza:
    print(p)
print("\n")
print("My friends favourite pizzas are: \n")

for p in friend_pizzas:
    print(p)
print("\n")

#4-13  More Loops
food = ("mac & cheese", "pizza", "bbq")
