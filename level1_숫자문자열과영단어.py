def solution(s):
    answer = ""
    number = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    num = ""
    for c in s:
        if c.isdigit():
            answer += c
        else:
            num += c
            if num in number.keys():
                answer += number[num]
                num = ""
    return int(answer)
