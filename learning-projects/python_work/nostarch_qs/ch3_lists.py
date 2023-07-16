#3-1 Names

friends = ["clarence", "john", "mick"]

print(friends[0])
print(friends[1])
print(friends[2] +"\n")

#3-2 Greetings

print("Hello " + friends[0])
print("Hello " + friends[1])
print("Hello " + friends[2] +"\n")

#3-4 Guest List

guest = ["Joe Rogan", "Elon Musk", "Michael Jordan"]
print("Hi " + guest[0] + ". You are invited to my dinner party")
print("Hi " + guest[1] + ". You are invited to my dinner party")
print("Hi " + guest[2] + ". You are invited to my dinner party\n")

#3-5 Changing Guest List

print(guest[0] + " can't make it")
guest[0] = "Jonny Depp"
print("Hi " + guest[0] + ". You are invited to my dinner party")
print("Hi " + guest[1] + ". You are invited to my dinner party")
print("Hi " + guest[2] + ". You are invited to my dinner party\n")

#3-6 More Guests 

print("We have found a bigger dinner table!\n")
guest.append("Doctor Who")
guest.append("Ratchet")
guest.append("Clank")
for i in guest:
    print(i + " You are invited to my dinner party!")
print("\n")
                                                                                
#3-7 Shrinking Guest List

print("I can only invite 2 people to dinner\n")
while len(guest) > 2: 
    print("I'm sorry " + guest[-1] + ". You don't make the cut")
    del guest[-1]
else: print(f"Congratulations {guest[0]} and {guest[1]}, you're still invited!")

for n in range(1, (len(guest)-1)):
    guest.pop(0)
    print(guest)

#3-8 Seeing The World

places = ["Rome", "Paris", "Bahamas", "Maldives", "South America"]

print("\n" + places)
print(sorted(places))
print(places)
print(places.reverse)
print(places.sort())
