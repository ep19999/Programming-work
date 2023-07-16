#1
#for i in range(1500, 2701):
#    if i % 7 == 0 and i % 5 == 0:
#        print(i)

#2
#for i in range(0, 7):
#    if i % 3 == 0:
#        continue
#    else:
#        print(i)

#3
#for i in range(0, 51):
#    if i % 3 == 0 and i % 5 == 0:
#        print("FizzBuzz")
#    elif i % 3 == 0:
#        print("Fizz")
#    elif i % 5 == 0:
#        print("Buzz")
#    else:
#        print(i)

#4
#evens = []
#for i in range(100, 401):
#    if i % 2 == 0:
#        evens.append(str(i))
#result = ' ,'.join(evens)
#print(result)

#5
#number = int(input("Enter number between 0-10,000,000: "))
#prime = "False"
#   
#for i in range(2,10000001):
#    if number % i == 0 and i != number:
#        print("number is not prime")
#        break
#    elif i == 1000000:
#        print("number is prime")

#6
#def find_max(num1, num2, num3):
#    numbers = [num1, num2, num3]
#    max_num = max(numbers)
#    return max_num
#
#print("Please enter three numbers below:\nNOTE: press enter key after each number")
#num1, num2, num3 = int(input()),int(input()),int(input())
#print(find_max(num1, num2, num3))

#7
#import random as r
#target = r.randint(1, 9)
#while True:
#    guess = int(input("Try and guess the number between 1 - 9: "))
#    if guess != target:
#        print("Nope try again :(")
#    else:   
#        print(f"Well done the number was {guess}!!")
#        break
    
#8
#def str_rev(string):
#    rev_string = string[::-1]
#   return rev_string    
    
#string = input("Please enter a string to reverse: ")
#print(str_rev(string))

#9 
#def case_check(string):
#    '''Returns number of each case in given string in th format:
#    (num_lowercase, num_uppercase)'''
#    
#    upper = 0
#    lower = 0
#    for i in range(0, len(string)):
#        if string[i].islower():
#            lower += 1
#        else:
#            upper += 1
#    return lower, upper
#
#print(case_check("HaHaHa"))

#10 
#print("Please choose number corresponding to meat type:")
#meat = int(input("1 Beef (well done)\n2 Chicken\n3 Lamb\n4 Pork\nENTER: ")) 
#if meat == 1:
#    weight = int(input("How heavy is it (Kg)?: "))
#    meat_type = "Beef"      
#    time = (weight * 50) + 20
#    print(f"The cooking time for a piece of {meat_type} that weighs{weight}Kg is {time}mins")
#elif meat == 2:
#    weight = int(input("How heavy is it (Kg)?: ") )
#    meat_type = "Chicken"
#    time = (weight * 45) + 20
#    print(f"The cooking time for a piece of {meat_type} that weighs{weight}Kg is {time}mins")
#elif meat == 3:
#    weight = int(input("How heavy is it (Kg)?: "))
#    meat_type = "Lamb"
#    time = (weight * 60) + 30
#    print(f"The cooking time for a piece of {meat_type} that weighs{weight}Kg is {time}mins")
#elif meat == 4:
#    weight = int(input("How heavy is it (Kg)?: "))
#    meat_type = "Pork"
#    time = (weight * 70) + 35
#    print(f"The cooking time for a piece of {meat_type} that weighs {weight}Kg is {time}mins")
#else: 
#    print("Please enter a valid meat code")

#11
import time
print("Rock paper scissors game starting")
run = 'Y'
while run == 'Y'
    p1 = input("Player 1 enter Rock Paper or Scissors: ")
    p2 = input("Player 2 enter Rock Paper or Scissors: ")
    if p1 == p2:
        run = ("Match is a draw, do you want to play again? Y/N: ")
    if p1 == 'Rock' & p2 == 'scissors':
    if p1 == 'Rock' & p2 == 'paper':
    if 
   
    












        


