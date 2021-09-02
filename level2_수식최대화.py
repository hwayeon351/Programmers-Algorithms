from itertools import permutations
from collections import deque
def solution(expression):
    answer = 0
    #1. 연산자와 피연산자 split
    nums = []
    op = []
    ori_operation = []
    num = ""
    n = 0
    for e in expression:
        if e.isdigit():
            num += e
        else:
            n = int(num)
            nums.append(n)
            ori_operation.append(n)
            num = ""
            op.append(e)
            ori_operation.append(e)
    n = int(num)
    nums.append(n)
    ori_operation.append(n)
    
    #2. 연산자 우선순위 조합 구하기
    op_kinds = list(set(op))
    op_permu = permutations(op_kinds, len(op_kinds))
    
    #3. 계산하기
    op_stack = []
    operation_stack = []
    for per in op_permu:
        operation = deque(ori_operation[:])
        operation_stack = []
        op_stack = list(per)
        while True:
            if len(operation) == 0:
                if len(operation_stack) == 1:
                    result = abs(operation_stack[-1])
                    if result > answer: answer = result
                    break
                operation = deque(operation_stack)
                operation_stack = []
                op_stack.pop()
            k = operation.popleft()
            if str(k).isdigit():
                operation_stack.append(k)
            elif k == op_stack[-1]:
                n1 = operation_stack.pop()
                n2 = operation.popleft()
                if k == '+':
                    n3 = n1+n2
                elif k == '-':
                    n3 = n1-n2
                elif k == '*':
                    n3 = n1*n2
                operation_stack.append(n3)
            else: operation_stack.append(k)

    return answer
