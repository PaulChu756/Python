
first = [] 
last = []
f = open("classNames.txt" , "r")
f.read()
for names in f:
	names = names.replace("\n" , " ")
for names in f:
	if names.lower() in f:
		first.append(f)
	else: 
		last.append(f)
print (names)
