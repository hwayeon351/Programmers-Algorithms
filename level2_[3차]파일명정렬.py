def solution(files):
    answer = []
    filenames = []
    for idx, file in enumerate(files):
        head = ""
        for i in range(len(file)):
            if file[i].isdigit():
                break
            head += file[i]
            
        number = ""
        for j in range(i, len(file)):
            if file[j].isdigit():
                number += file[j]
            else: break
        number = number.lstrip('0')
        
        filenames.append([idx, head.lower(), int(number) if len(number) > 0 else 0])
        
    filenames.sort(key = lambda x:(x[1], x[2], x[0]))
    for file in filenames:
        answer.append(files[file[0]])
    
    return answer
