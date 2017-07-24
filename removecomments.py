import sys
retval = ""
for l in sys.stdin:
	if "#" in l:
		myoff = int(l[l.find("#")+2:].split()[0], 16)
		l = l[:l.find("#")]
		if 2*(myoff + 2) != len(retval):
			print("myoff fail:", hex(myoff), hex(len(retval)//2 - 2), file=sys.stderr)
		#print(hex(len(retval)//2 - 2 + 0x217014))
	l = l.strip()
	retval += l
print(retval)
