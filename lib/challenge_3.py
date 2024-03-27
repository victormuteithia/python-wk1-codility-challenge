#Challenge 3
import random

def solution(N):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    num_of_repetitions = N // 26
    remainder = N % 26

    result = "".join([alphabet * num_of_repetitions])
    result += alphabet[:remainder]
    results_list = list(result)
    random.shuffle(results_list)
    # return results_list
    return "".join(results_list)

print(solution(3))
print(solution(7))
print(solution(30))
    
