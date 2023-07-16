def filterFunc(x):
    if x % 2 == 0:
        return False
    return True

def filterFunc2(x):
    if x.isupper():
        return False
    return True

def squareFunc(x):
    return x**2

def toGrade(x):
    if x >= 90:
        return "A"
    elif x >= 80 and x < 90:
        return "B"
    elif x >= 70 and x < 80:
        return "C"
    else:
        return "D"



def main():
    nums = (3, 4, 23, 35, 58, 323, 12493, 2355, 2324)
    chars = "abcdEFghIjkLMNop"
    grades = (81, 89, 94, 78, 61, 66, 99, 74)

    # Use filter to remove from a list.
    odds = list(filter(filterFunc, nums))
    print(odds)

    # Filter on non numeric list
    lowers = list(filter(filterFunc2, chars))
    print(lowers)

    # Use map to create new sequence of values
    squares = list(map(squareFunc, nums))
    print(squares)

    # Use sorted and map to change numbers to grades
    grades = sorted(grades)
    letters = list(map(toGrade, grades))
    print(letters)


if __name__ == "__main__":
    main()