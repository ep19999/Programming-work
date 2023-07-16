def hextoDec(hex_num):
    import string
    total = 0
    numbers = len(hex_num)
    count = 1
    
    if all(c in string.hexdigits for c in hex_num):
        for i in range(0, (numbers)):
            if hex_num[i] == "A":
                total += (10 * (16 ** (numbers - count)))
                count += 1
            elif hex_num[i] == "B":
                total += (11 * (16 ** (numbers - count)))
                count += 1
            elif hex_num[i] == "C":
                total += (12 * (16 ** (numbers - count)))
                count += 1
            elif hex_num[i] == "D":
                total += (13 * (16 ** (numbers - count)))
                count += 1
            elif hex_num[i] == "E":
                total += (14 * (16 ** (numbers - count)))
                count += 1
            elif hex_num[i] == "F":
                total += (15 * (16 ** (numbers - count)))
                count += 1
            else:
                total += int(hex_num[i]) * 16 ** (numbers - count)
                count += 1
    else: 
        total = None
    return total

print(hextoDec("ABC1234F"))          

