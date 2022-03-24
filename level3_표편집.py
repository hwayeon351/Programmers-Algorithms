def solution(n, k, cmd):
    check = ['O']*n
    linked_list = {i:[i-1, i+1] for i in range(n)}
    stack = []
    cursor = k
    for command in cmd:
        if command[0] == 'U':
            x = int(command.split(" ")[1])
            for _ in range(x):
                cursor = linked_list[cursor][0]
            
        elif command[0] == 'D':
            x = int(command.split(" ")[1])
            for _ in range(x):
                cursor = linked_list[cursor][1]
                
        elif command[0] == 'C':
            prev, next = linked_list[cursor][0], linked_list[cursor][1]
            check[cursor] = 'X'
            stack.append([prev, next, cursor])
            if prev == -1:
                linked_list[next][0] = prev
                cursor = next
            elif next == n:
                linked_list[prev][1] = next
                cursor = prev
            else:
                linked_list[prev][1] = next
                linked_list[next][0] = prev
                cursor = next
            
        elif command[0] == 'Z':
            prev, next, idx = stack.pop()
            check[idx] = 'O'
            linked_list[idx][0] = prev
            linked_list[idx][1] = next
            if prev == -1:
                linked_list[next][0] = idx
            elif next == n:
                linked_list[prev][1] = idx
            else:
                linked_list[prev][1] = idx
                linked_list[next][0] = idx
            
    return "".join(check)
