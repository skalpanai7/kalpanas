l=[int(x) for x in raw_input().split()]
temp=l[0]
for i in range(len(l)):
	if temp>l[i]:
		temp=l[i]
	elif temp<l[i]:
		pass
	else:
		temp=l[i]
print temp
