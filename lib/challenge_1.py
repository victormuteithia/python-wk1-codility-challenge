#Challenge 1

# i = index

def solution(array):
    count = 0
    for i, num in enumerate(array): # turns the array into an enumerate object
        if num != 10 and i + 1 < len(array):
            moves = 10 - num
            count += abs(moves)
            array[i + 1] = array[i + 1] - moves
    
    if array[-1] != 10:
        return -1
    else:
        return count
    
print(solution([7, 15, 10, 8])) # ([10, 10, 10, 10]), so print 7
print(solution([11, 10, 8, 12, 8, 10, 11])) # ([10, 10, 10, 10, 10, 10, 10]), so print 6
print(solution([7, 14, 10])) # ([10, 10, 11]), so print -1



