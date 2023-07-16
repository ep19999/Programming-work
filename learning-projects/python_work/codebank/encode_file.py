from encode_string import encodeString
import os

def encodeFile(filename, newfilename):
    with open(filename) as file_object:
        for line in file_object:
                newfile = open(newfilename, 'a')
                data = encodeString(line)
                newData = [f'{char}{count}' for char, count in data]
                newfile.write(str(newData))
                newfile.close()

print(os.path.getsize('artfile.txt'))
encodeFile('artfile.txt', 'codeartfile.txt')
print(os.path.getsize('codeartfile.txt'))

