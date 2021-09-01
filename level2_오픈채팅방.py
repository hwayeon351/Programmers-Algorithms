def solution(record):
    answer = []
    user_dict = dict()
    for r in record:
        cmd = r.split()
        if cmd[0] == 'Enter':
            if cmd[1] not in user_dict: user_dict[cmd[1]] = cmd[2]
            else: user_dict[cmd[1]] = cmd[2]
        elif cmd[0] == 'Change':
            user_dict[cmd[1]] = cmd[2]
    for r in record:
        cmd = r.split()
        if cmd[0] == 'Enter':
            answer.append(user_dict[cmd[1]] + "님이 들어왔습니다.")
        elif cmd[0] == 'Leave':
            answer.append(user_dict[cmd[1]] + "님이 나갔습니다.")
    
    return answer
