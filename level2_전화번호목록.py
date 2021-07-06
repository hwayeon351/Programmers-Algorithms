def solution(phone_book):
    phone_dict = dict()
    for p in phone_book:
        phone_dict[p] = 1
    for p in phone_book:
        temp = ""
        for n in p[:-1]:
            temp += n
            if temp in phone_dict: return False
    return True
