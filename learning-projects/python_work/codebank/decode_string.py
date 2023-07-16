def decodeString(inputs):
    decoded = ''
    for t in inputs:
        decoded += t[0] * t[1]
    return decoded

lsdf = [('A', 1), ('B', 1), ('C', 1), ('D', 3), ('E', 1)]

print(decodeString(lsdf))

