from collections import deque
def solution(people, limit):
    boat = 0
    people.sort(reverse = True)
    people = deque(people)
    while people:
        max_p = people.popleft()
        if len(people) > 0:
            min_p = people.pop()
            if max_p + min_p > limit:
                people.append(min_p)
        boat += 1
    return boat
