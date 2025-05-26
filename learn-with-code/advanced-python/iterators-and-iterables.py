# class definition that wil be act as iterators and iterable
class reverseList:
    # Assigning the data to the instance data as called
    def __init__(self,data):
        self.data = data
        self.index = len(data) 

    # a method which makes the class/object/instance iterators  
    def __iter__(self):
        return self 
    
    # method to return the next item in the list   
    def __next__(self):
        if self.index == 0:
            print("This is the end of the list")
            print("Program exit.")
            exit()       
        self.index = self.index -1
        return self.data[self.index]
    
# list object
num_list = [1,2,3,4,5]

# created an iterator instance of the class reverseList by just passing a data to it
reversed_list = reverseList(num_list)

# using within the loop
for item in reversed_list:
    print(item)

# using with next()
print(next(reversed_list))
print(next(reversed_list))
print(next(reversed_list))
print(next(reversed_list))
print(next(reversed_list))
