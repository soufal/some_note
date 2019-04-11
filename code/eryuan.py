T = int(input())
re = []
for i in range(T):
    re.append(list(map(int,input().split())))
x,y=0,0
def abv(a1,b1,v1,a2,b2,v2):
	b3=b1*a2
	v3=v1*a2
	b4=b2*a1
	v4=v2*a1

	b5=b3-b4
	v5=v3-v4
	if b5==0:
		print("UNKNOWN")
	elif a1 == 0:
		y = v1/b1
		x = (-1*y*b2+v2)/a2
	else:
		y = v5/b5
		x = (-1*y*b1+v1)/a1
		if y>0 and x>0 and int(y)==y and int(x)==x:
			print(int(x),int(y))
		else:
			print("UNKNOWN")
for j in re:
    abv(j[0],j[1],j[2],j[3],j[4],j[5])
