from itertools import permutations
def solution(numbers):
    sosu = set()
    for i in range(1,len(numbers)+1):
        for c in permutations(list(numbers), i):
            num = int("".join(list(c)))
            #3. 소수 판별
            if num == 1 or num == 0: continue
            check = True
            for n in range(2,num//2+1):
                if num % n == 0:
                    check = False
                    break
            if check==False: continue
            sosu.add(num)
    return len(sosu)
