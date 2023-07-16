def encodeString(sequence):
    length = 1
    encoded = []
   
    for i in range(0, len(sequence)):
        if sequence[i] == sequence[-1]:
            encoded.append((sequence[i], length))
            length = 1
        elif sequence[i] == sequence[i+1]:
            length += 1
        elif sequence[i] != sequence[i+1]:
            encoded.append((sequence[i], length))
            length = 1
        
    return encoded

