#Challenge 2

#function to get the sum of the digits of a number
def add_digits(num):
    return sum(int(digit) for digit in list(str(num)))

def solution(A):
    #set the max sum to -1
    max_total_sum = -1
    # iterate through the range of the length of A
    for num1 in range(len(A)):
        #iterate through the range of the length of a start from the index after num1
        for num2 in range(num1 + 1, len(A)):
            #get the sum of the digits of num1 and num 2
            sum_of_digits1 = add_digits(A[num1])
            sum_of_digits2 = add_digits(A[num2])
            #if they are equal, get the sum of num1 and num2 and assign the greater value to max_total_sum 
            if sum_of_digits1 == sum_of_digits2:
                max_total_sum = max(max_total_sum, A[num1] + A[num2])
            #otherwise max_total_sum = -1
            else:
                max_total_sum = -1
        #return max_total_sum
        return max_total_sum
        
    
    


        
        # if number == sum_of_num1:
            # return sum_of_num1
        # if A[index] == A[index + 1]:
        #     pass

print(solution([51, 71, 17, 42])) #prints 93
print(solution([42, 33, 60])) #prints 102
print(solution([51, 32, 43])) #prints -1

