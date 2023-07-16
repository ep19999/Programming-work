#Strings not interchangeable with bytes. They are unicode ie utf-8, bytes raw 8-bit.
def main():

    b = bytes([0x41, 0x42, 0x43, 0x44])
    print(b)
    s = "This is a string"
    print(s)

    # To combine the two:
    s2 = b.decode('utf-8') #decode takes bytes and returns a string using utf-8 encoding.
    print(s+s2)
    b2 = s.encode('utf-8') #encode turns string into raw bytes
    print(b+b2)

    # encode with utf-32, turns string into hexadecimal:
    b3 = s.encode('utf-32')
    print(b3)    

if __name__ == "__main__":
    main()

