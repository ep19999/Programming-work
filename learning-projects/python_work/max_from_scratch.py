nums = [1, 5, 359834, 325, 242, 34235]

def fing_highest(arrays):
    cheese = len(arrays) #4
    
    while cheese > 1:
        print("running one iteration")
        if arrays[0] > arrays[1]:
            print(f"{arrays[1]} is smaller than {arrays[0]} - Removing")
            arrays.pop(1)
        elif arrays[0] < arrays[1]:
            print(f"{arrays[0]} is smaller than {arrays[1]} - Removing")
            arrays.pop(0)
        cheese -= 1
    return arrays[0]

print(fing_highest(nums))     
        
        

