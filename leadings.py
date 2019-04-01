leads = {}
order = []
varstk = []
var = {}
trails = {}

def Remove(duplicate): 
	final_list = [] 
	for num in duplicate: 
		if num not in final_list: 
      			final_list.append(num) 
	return final_list 

print("\n...............Leading of Operator precedence parser...........\n")
with open("input.txt") as infile:
	print("Productions are: ")
	for prods in infile:
		print(prods)
		c = prods[0]
		ind = prods.find('>')
		order.append(c)
		if prods.endswith('\n'):
			rhs = prods[ind+1:-1].split('|')
		else:
			rhs = prods[ind+1:].split('|')
		var[c] = rhs

print("Non terminals are: ",",".join(order))


#function To find all the leading

def Yadform(lst, varr, prod):
	#print("variables: ", varr,"productions: " ,prod)
	if ord(prod[0])>=65 and ord(prod[0])<=90:
		if prod[0]!=varr:
			#print("ifffffff")
			varstk.append(prod[0])
		if len(prod)>1:
			#print("ifffes")
			lst.append(prod[1])
	else:
		#print("elses")
		if prod[0]=='i':
			lst.append(prod[0:2])
		else:
			lst.append(prod[0])

#function to find the trailings

def daYform(lst, varr, prod):
	#print("variables: ", varr,"productions: " ,prod)
	if ord(prod[0])>=65 and ord(prod[0])<=90:
		if prod[-1]!=varr:
			#print("ifffffff")
			if not prod[-1] in varstk:
				varstk.append(prod[-1])
		if len(prod)>1:
			#print("ifffes")
			lst.append(prod[-2])
	else:
		#print("elses")
		if prod[-1]=='d':
			lst.append(prod[-2:])
		else: 
			lst.append(prod[-1])


for i in range(len(order)):
	#print("order here", order[i])
	#print("order vars", var[order[i]])
	lst = []
	for j in range(len(var[order[i]])):
		#print("order i ij",var[order[i]][j])
		Yadform(lst, order[i], var[order[i]][j])
		#print("templist", order[i],lst)
	#print("length of varialble stack: ", len(varstk))
	while len(varstk)!=0:
		ch = varstk.pop()
		for j in range(len(var[ch])):
			Yadform(lst,ch, var[ch][j])
		#print("inside the while loop", order[i], lst)
	#print("order lst", order[i], lst)
	leads[order[i]]=Remove(lst)
print("\n")
print("LEADINGS are: \n")

for key, value in leads.items() :
    print (key,": ", ", ".join(value))

#all leading computed. Now to calculate the trailings

del varstk[:]

for i in range(len(order)):
	#print("order here", order[i])
	#print("order vars", var[order[i]])
	lst = []
	for j in range(len(var[order[i]])):
		#print("order i ij",var[order[i]][j])
		daYform(lst, order[i], var[order[i]][j])
		#print("templist", order[i],lst)
	#print("length of varialble stack: ", len(varstk))
	while len(varstk)!=0:
		ch = varstk.pop()
		for j in range(len(var[ch])):
			daYform(lst,ch, var[ch][j])
		#print("inside the while loop", order[i], lst)
	#print("order lst", order[i], lst)
	trails[order[i]]=Remove(lst)
print("\n")
print("TRAILINGS are: \n")

for key, value in trails.items() :
    print (key,": ", ", ".join(value))

	
		

