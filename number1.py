string=raw_input()
ch=0
di=0
for i in string:
	if i.isdigit():
		di=di+1
	else:
		ch=ch+1
if(di>0 and ch>0):
	print "Yes"
else:
	print "No"
