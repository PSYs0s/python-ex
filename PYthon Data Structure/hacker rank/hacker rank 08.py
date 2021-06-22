k = int(input())
room_nums = map(int, input().split())

from collections import Counter
counts = Counter(room_nums)
for num, count in counts.items():
    if count != k:
        print(num)
        break
