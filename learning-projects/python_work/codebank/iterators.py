def main():
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    daysSp = ["Dom", "Lun", "Mar", "Mie", "Jue", "Vie", "Sab"]

    # iter creates an iterator over a collection.
    i = iter(days)
    print(next(i))
    print(next(i))
    
    # Can combine iter with a function, and a sentinel(Tells iter() when to stop calling the function)
    with open("testfile.txt", "r") as file:
        for line in iter(file.readline, ''):
            print(line.rstrip())

    # Use enumerate to reduce code and provide a counter
    for i,m in enumerate(days, start=1):
        print(i, m)
    
    # Use zip to combine sequences. Zip terminates where the shortest sequence ends if they are not the same length.
    for i,m in enumerate(zip(days, daysSp), start=1):
        print(i, m[0], "=", m[1], "in Spanish")

if __name__ == "__main__":
    main()