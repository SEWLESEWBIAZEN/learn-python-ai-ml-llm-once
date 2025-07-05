def sum_of_unmarked_values(values):
    n=len(values)
    marked = [False] * n
    sum = 0
    while True:
        smallest_number = float('inf')
        index = -1
        for i in range(n):
            if not marked[i] and smallest_number > values[i]:
                smallest_number = values[i]
                index = i
        if index == -1:
            break
        sum += smallest_number        
        marked[index] = True
        marked[index-1] = True if index > 0 and not marked[index-1] else marked[index-1]        
        if(index+1 < n):
            if not marked[index+1]:
                marked[index+1] = True                
        if all(marked):
            break
    return sum
total_points = sum_of_unmarked_values([10, 2, 3, 11,6, 5])
print(total_points) 

