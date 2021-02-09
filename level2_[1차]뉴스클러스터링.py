def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    arr1 = []
    arr2 = []
    inter = 0
    for i in range(len(str1)-1):
        if (str1[i]+str1[i+1]).isalpha():
            arr1.append(str1[i]+str1[i+1])
    for i in range(len(str2)-1):
        if (str2[i]+str2[i+1]).isalpha():
            arr2.append(str2[i]+str2[i+1])
    if len(arr1) == 0 and len(arr2) == 0: return 65536
    arr1.sort()
    arr2.sort()
    last = ""
    for a in arr1:
        if a == last: continue
        cnt = arr2.count(a)
        if cnt > 1:
            inter += min(cnt, arr1.count(a))
            last = a
            continue
        inter += cnt
        last = a

    return int(inter / (len(arr2) - inter + len(arr1)) * 65536)
