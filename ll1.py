from ffl import *
partab = {}

def check_non_ter(val):
	if ord(val)>=60 and ord(val)<=90:
		#print("true non terminal")
		return True
	else:
		#print("not non terminal")
		return False

def put_int_tab(v, prods):
	if check_non_ter(prods[0]):
		for i in first[prods[0]]:
			if(partab.get(v)==None):
				partab[v]={}
			partab[v][i]=str(v+"->"+prods)
	elif prods[0]=='e':
		for j in follow[v]:
			if(partab.get(v)==None):
				partab[v]={}
			partab[v][j]=str(v+"->"+prods)
	else:
		if(partab.get(v)==None):
				partab[v]={}
		partab[v][prods[0]]=str(v+"->"+prods)


def build_table():
	for v in order:
		for i in range(len(var[v])):
			#print("Building the table",v ,var[v][i])
			put_int_tab(v, var[v][i])

def parse_it(instr):
	lst = []
	instr+='$'
	lst.append('$')
	lst.append(order[0])
	i=0
	while i<len(instr):
		print("".join(lst),'\t',instr[i:len(instr)])
		top = lst.pop()
		#print("top is: ",top)
		if check_non_ter(top):
			if instr[i]=='i' and top!='F':
				v_prod = partab[top][instr[i:i+2]]
			else:
				v_prod = partab[top][instr[i]]
			#print("working", v_prod)
			for j in range(len(v_prod)-1,2,-1):
				if v_prod[j]!='e':
					lst.append(v_prod[j])
		elif instr[i]==top:
			if instr[i]=='$':
				print("String successfully parsed")
				break
			else:
				#print("input_symbol matched")
				i+=1
		


print("\n\n..............Predictive Parsing(LL-1).............\n")
print("order: ", order)
build_table()

for key, value in partab.items() :
	print("\n", key)
	for k, val in partab[key].items():
    		print (k,": ", "".join(val))

#print("The parse table is: ",partab)

print("\n")
instr = input("Enter the string to be parsed:")
print("\n")
parse_it(instr)
