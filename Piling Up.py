from collections import deque

for _ in range(int(input())):
    size = int(input())
    block = deque(list(map(int, input().split())))
    possibility = True
    
    for _ in range(len(block)):
        if block[0] >= block[1]:
            block.popleft()
        elif block[-1] >= block[-2]:
            block.pop()
        else:
            possibility = False
            
    if possibility :
        print('Yes')
    else:
        print('No')