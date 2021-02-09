def solution(dartResult):
    bonus = ['S', 'D' ,'T']
    op = ['*', '#']
    cnt = -1
    arr = []
    for i in range(len(dartResult)):
        if dartResult[i] in bonus:
            if dartResult[i] == 'D':
                arr[cnt] = arr[cnt] ** 2
            elif dartResult[i] == 'T':
                arr[cnt] = arr[cnt] ** 3

        elif dartResult[i] in op:
            if cnt == 0:
                if dartResult[i] == '*':
                    arr[cnt] = arr[cnt] * 2
                if dartResult[i] == '#':
                    arr[cnt] = arr[cnt] * -1
            else:
                if dartResult[i] == '*':
                    arr[cnt] = arr[cnt] * 2
                    arr[cnt-1] = arr[cnt-1] * 2
                elif dartResult[i] == '#':
                    arr[cnt] = arr[cnt] * -1
        else:
            if dartResult[i] == '0':
                if dartResult[i-1].isdigit():
                    arr[cnt] = int(dartResult[i-1]+dartResult[i])
                    continue
            cnt += 1
            arr.append(int(dartResult[i]))
    return sum(arr)
