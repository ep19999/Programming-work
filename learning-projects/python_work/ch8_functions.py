#8-1 Message
#def display_message():
#    '''prints a sentence'''
#    print("Here we are learning all about functions")

#8-2 Favorite Book
#def favorite_book(title):
#    print(f"One of my favourite books is {title}")
#
#favorite_book("Hunger Games")

#8-3 T-Shirt
#def make_shirt(size, text='no text'):
#    print(f'The shirt will be size {size} and have {text} on it.')
#
#make_shirt("small", "wah")

#8-4 Large Shirt 
#def make_shirt2(size='',text='i love python'):
#    print(f'The shirt will be size {size} and read {text}')

#8-5 Cities
#def describe_city(city, country):
#    print(f"{city} is in {country}")

#8-6 City Names
#def city_country(city, country):
#    '''Takes city-country pairs and returns in a list'''
#    return f"{city}, {country}"

#print(city_country("London", "England"))
    
#8-7 Album
#def make_album(name, title):
#    album = {'name': name, 'title': title}
 #   return album

#print(make_album("hgoewg", "hello"))

#8-8 Use Albums
#run = 'Y'
#while run == 'Y':
#    name = input("Enter Artist: ")
#    title = input("Enter album title: ")
#    print(make_album(name, title))
#    y = input("Would you like to add more? Y/N: ")
#    if y == 'Y':
#        continue
#    elif y == 'N':
#        break
#    else: 
#        print("invalid")

# #8-9 Magicians
# magicians = ["Gary", "Angela", "Paul"]

# def show_magicians(list):
#     for i in list:
#         print(i)

#8-10 
#def make_great(list):
#    for i in range(0, len(list)):
#        list[i] += " the Great"
 #    return list
#make_great(magicians)
#show_magicians(magicians)

#8-11
#def make_great(list):
    for i in range(0, len(list)):
        list[i] += " the Great"
    return list

# Great_magicians = make_great(magicians[:])
# show_magicians(magicians)
# show_magicians(great_magicians)

#8-12 Sandwiches
# def sandwich_build(*fillings):
#     for i in fillings:
#         print(f"adding {i} to your sandwich")
#         print("Your sandwich is ready!")

# sandwich_build('cheese', 'ham')

# #8-13 User Profile
# def build_profile(first, last, **user_info):
#     """Build a dictionary containing everything we know about a user."""
#     profile = {}
#     profile['first_name'] = first
#     profile['last_name'] = last
#     for key, value in user_info.items():
#         profile[key] = value
#     return profile


# my_profile = build_profile('Elliot', 'Penny',
#                             ethnicity='Caucasian',
#                             work='Chef')

# print(my_profile)

# #8-14 Cars
# def make_car(manufacturer, name, **car_info):
#     car_profile = {}
#     car_profile['manufacturer'] = manufacturer
#     car_profile['model'] = name
#     for key, value in car_info.items():
#         car_profile[key] = value
#     return car_profile

# car = make_car('Honda', 'Civic', type='R', engine_size='1.8L', colour='Black')
# print(car)

#8-15 Printing Models
