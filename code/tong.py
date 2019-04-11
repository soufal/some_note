T = int(input())
n=[]
tong=[]
result=[]
for i in range(T):
    n.append(int(input()))
    tong.append(list(map(int,input().split())))
def compute_qu(mood):
    s = 0
    left_index = 0
    right_index = len(mood)-1
    left = mood[0]
    right = mood[-1]
    while len(mood)>1:
        for i in range(1,len(mood)):
            mid_index = 0
            if mood[i] >= mood[0]:
                mid = mood[i]
                mid_index = i
                break
        if mid_index != left_index:
            s = s + (mid_index - left_index) * mood[0]
            mood = mood[mid_index:right_index]
            left_index = mid_index
        else:
            for j in range(1,len(mood)):
                mid_index = right_index
                if mood[-1] <= mood[-j]:
                    mid_index = len-j
                    mid = mood[-j]
                    break
                if mid_index != right_index:
                    s = s+(mid_index - right_index) * mood[-1]
                    mood = mood[left_index:mid_index]
                    right_index=mid_index
    resule.append(s)
for j in tong:
    compute_qu(tong)
for i in result:
    print(i,end='\n')
T = int(input())
n=[]
tong=[]
result=[]
for i in range(T):
    n.append(int(input()))
    tong.append(list(map(int,input().split())))
def compute_qu(mood):
    s = 0
    left_index = 0
    right_index = len(mood)-1
    left = mood[0]
    right = mood[-1]
    while len(mood)>1:
        for i in range(1,len(mood)):
            mid_index = 0
            if mood[i] >= mood[0]:
                mid = mood[i]
                mid_index = i
                break
        if mid_index != left_index:
            s = s + (mid_index - left_index) * mood[0]
            mood = mood[mid_index:right_index]
            left_index = mid_index
        else:
            for j in range(1,len(mood)):
                mid_index = right_index
                if mood[-1] <= mood[-j]:
                    mid_index = len-j
                    mid = mood[-j]
                    break
                if mid_index != right_index:
                    s = s+(mid_index - right_index) * mood[-1]
                    mood = mood[left_index:mid_index]
                    right_index=mid_index
    resule.append(s)
for j in tong:
    compute_qu(tong)
for i in result:
    print(i,end='\n')
