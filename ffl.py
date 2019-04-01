import numpy as np

var={}
varstk=[]
first={}
follow={}
order=[]

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
		var[c]=rhs

print("The non terminals are: ",", ".join(order))

def ialform(lst, var, prod):
	#print("Prods", prod)
	if ord(prod[0])>=65 and ord(prod[0])<=90 and prod[0]!=var:
		varstk.append(prod[0])
	else:
		if prod[0]=='i':
			lst.append(prod[0:2])
		else:
			lst.append(prod[0])

def FIRST():
	for v in order:
		lst=[]
		for i in range(len(var[v])):
			ialform(lst, v, var[v][i])
			#print("\n")
		while len(varstk)!=0:
			val = varstk.pop()
			#print("from stk ",val)
			for i in range(len(var[val])):
				#print("inside this loop: ",var[val][i], len(var[val]), val)
				ialform(lst, val,var[val][i])
		first[v]=lst
	for key, value in first.items() :
    		print (key,": ", ", ".join(value))

def getfollows(val):
	#print("In the get follow function: value of val", val)
	lst=[]
	for v in order:
		for rhs in var[v]:
			#print("value ",v)
			#print("rhs", rhs)
			ind = rhs.find(val)
			#print("index: ", ind)
			if ind>=0:
				if ind==len(rhs)-1:
					lst = lst+follow[v]
					#print("folows: ",lst)
				elif 65<=ord(rhs[ind+1])<=90:
					#print("I am here")
					for eles in first[rhs[ind+1]]:
						if eles!='e':
							lst.append(eles)
					if 'e' in first[rhs[ind+1]]:
						lst = lst+follow[v]
					#print("appended",lst)
				elif ord(rhs[ind+1])<65 or ord(rhs[ind+1])>=91:
					lst.append(rhs[ind+1])
					#print("Appended",rhs[ind+1],lst)
	#print("tempList",lst)
	return lst;

def FOLLOW():
	for v in order:
		follow[v]=[]
	for coup in enumerate(order):
		val = coup[1]
		#print("coup",coup[1])
		follow[val] = list(set(getfollows(val)))
		if coup[0]==0:
			follow[val].append('$')
	for key, value in follow.items() :
    		print (key,": ", ", ".join(value))
	
print("\nThe FIRST of each productions are: ")
FIRST()
print("\nThe FOLLOW of each productions are: ")
FOLLOW()		
