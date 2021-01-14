from math import gcd
def get_lcm(a, b):
    return a * b // gcd(a, b)

def solution(arr):
    lcm = arr[0]
    for i in arr[1:]:
        lcm = get_lcm(lcm, i)
    return lcm
