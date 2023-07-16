#9-1 Restaraunt
# class Restaraunt():
#     '''model of a restaurant'''
    
#     def __init__(self, name, type):
#         self.name = name
#         self.type = type

#     def describe_restaurant(self):
#         print(f"This is a {self.type} Restaurant called {self.name}")
    
#     def open_restaurant(self):
#         print(f"{self.name} is open for business")

# crispys = Restaraunt('crispys', 'chippie')

# print(crispys.name)
# print(crispys.type)
# print(crispys.describe_restaurant())
# print(crispys.open_restaurant())

#9-2 Three Restaurants
# rnt1 = Restaraunt('Anukka', 'Indian')
# rnt2 = Restaraunt('Golden Dragon', 'Chinese')
# rnt3 = Restaraunt('Giggling Squid', 'Thai')
# print(rnt1.describe_restaurant())
# print(rnt2.describe_restaurant())
# print(rnt3.describe_restaurant())

#9-3 Users
# class User():
#     def __init__(self, first_name, last_name, password, user_name):
#         self.first = first_name
#         self.last = last_name
#         self.passwd = password
#         self.uname = user_name
    
#     def describe_user(self):
#         print(f"{self.first} {self.last}, password: {self.passwd}, username: {self.uname}")

#     def greet_user(self):
#         print(f'Hello {self.first} have a great day!')

# user1 = User('Elliot', 'Penny', 'qwerty', 'epenz')
# # user2 = User('John', 'Smith', 'wordpass', 'Jonnyboi' )

# user1.describe_user()
# user2.greet_user()

#9-4 Number Served
#using exercise 9-1

class Restaraunt():
    '''model of a restaurant'''
    
    def __init__(self, name, type, number_served=0):
        self.name = name
        self.type = type
        self.number_served = number_served

    def describe_restaurant(self):
        print(f"This is a {self.type} Restaurant called {self.name}")
    
    def open_restaurant(self):
        print(f"{self.name} is open for business")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number 


# restaurant = Restaraunt("Wong's", 'Chinese')
# print(restaurant.number_served)

# restaurant.number_served = 46
# print(restaurant.number_served)

# restaurant.set_number_served(90)
# print(restaurant.number_served)

# restaurant.increment_number_served(15)
# print(restaurant.number_served)

class IceCreamStand(Restaraunt):
    def __init__(self, *flavour):
        self.flavour = flavour

    def list_flavours(self):
        print(self.flavour)

exe = IceCreamStand("cream_yourself", "Ice Cream", 0, 'choc', 'strawb', 'mint')
exe.list_flavours()
      








