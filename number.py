number,rep=map(int,raw_input().split())
list=[int(x) for x in raw_input().split()]
c=0
for i in range(number):
	if list[i]==rep:
		c=c+1
print c
