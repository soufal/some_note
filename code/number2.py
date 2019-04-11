def number(n,date):
    group=lambda x:x[1] - x[0]
    for i, j in groupby(enumerate(date), group):
        l1=[k for g,k in j]
        if len(l1)>2:
            temp=str(min(l1)) + '-' + str(max(l1))
        elif len(l1)>1:
            temp=str(l1[0]) + ' ' +str(l1[1])
        else:
            temp = l1[0]
        print(temp, end=' ')

if __name__ == '__main__':
    n=int(input())
    date=list(map(int,input().split()))
    number(n,date)