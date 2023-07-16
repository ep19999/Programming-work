#old way to open a file
#with open('file.txt') as file_object:
#    contents = file_object.read()
#    print(contents)

#opening a file and specifying num characters
# file = open("file.txt", "r")
# print(file.read(50))

#new way to open files with pathlib
# from pathlib import Path
# file = Path("file.txt")
# f = open(file)
# print(f.read())

#10-1 Learning Python
#print out whole file
with open('learning_python.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

#line by line
with open('learning_python.txt') as file_object:
    for line in file_object:
        print(line.rstrip())

#store as a list where each object is a line of text
with open('learning_python.txt') as file_object:
   file = file_object.readlines()
print(file)
for line in file:
    print(line.rstrip())

#10-2 Learning C
#with open('learning_python.txt') as file_object:
#    print(contents.replace('Python', 'C'))
#    contents = file_object.read()

with open('learning_python.txt') as file_object:
    for line in file_object:
        print(line.replace('Python', 'C').rstrip())

#10-3 Guest
#name = input("Please enter your name: ")
#with open('guest_name.txt', 'w') as file_object:
#    file_object.write(name)

#file_object = open('guest_name2.txt', 'w')
#file_object.write(name)

#10-4 Guest Book
# while True:
#     name = input("Please enter your name: ")
#     file_object = open('guest_book.txt', 'a')
#     file_object.write(f"{name}\n")
#     run = input("add another line? y/n? ").lower()
#     if run == 'y':
#         continue
#     elif run == 'n':
#         break

#10-5 Programming Poll
# while True:
#     response = input("Why do you like programming?: ")
#     file_object = open('programming_poll.txt', 'a')
#     file_object.write(f"{response}\n")
#     run = input("add another entry? y/n? ").lower()
#     if run == 'y':
#         continue
#     elif run == 'n':
#         break






    

    







