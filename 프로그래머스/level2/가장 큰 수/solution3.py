from itertools import permutations 
def solution(numbers): 
    permute = list(permutations(numbers,len(numbers))) #몇개의 순열을 생성할건지
    list_permute = list(map(lambda i: ''.join(map(str,i)),permute))
    return max(list_permute) 