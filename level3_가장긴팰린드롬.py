import sys
sys.setrecursionlimit(7000000)
def palindrome(left, right, s, visit):
    global answer
    if visit[left][right] == 1: return
    visit[left][right] = 1
    l, r = left, right
    ck = True
    while l<=r:
        if s[l] != s[r]:
            if left+1 <= right: palindrome(left+1, right, s, visit)
            if right-1 >= left: palindrome(left, right-1, s, visit)
            ck = False
            break
        l+=1
        r-=1
    if ck == True:
        cnt = right-left+1
        if answer < cnt: answer = cnt
            
def solution(s):
    global answer
    answer = 1
    visit = [[0]*len(s) for i in range(len(s))]
    palindrome(0, len(s)-1, s, visit)

    return answer
