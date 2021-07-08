liste = input().strip().split(" ")
print(liste)
operand = ["+","*","-","/"]
sayac = 0
newlist=[]
kontrol=0
while "+" in liste or "-" in liste or "*" in liste or "/" in liste:
	while sayac<=(len(liste)-2): # 5       + + 1 2 3 || + 3 
		if (sayac+1)<len(liste) and (sayac+2)<len(liste) and liste[sayac]=="+" and not (liste[sayac+1] in operand) and not (liste[sayac+2] in operand):
			print(str(float(liste[sayac+1])+float(liste[sayac+2])))
			newlist.append(str(float(liste[sayac+1])+float(liste[sayac+2])))
			sayac+=2
		elif (sayac+1)<len(liste) and (sayac+2)<len(liste) and liste[sayac]=="*" and not (liste[sayac+1] in operand) and not (liste[sayac+2] in operand):
			print(str(float(liste[sayac+1])*float(liste[sayac+2])))
			newlist.append(str(float(liste[sayac+1])*float(liste[sayac+2])))
			sayac+=2
		elif (sayac+1)<len(liste) and (sayac+2)<len(liste) and liste[sayac]=="-" and not (liste[sayac+1] in operand) and not (liste[sayac+2] in operand):
			print(str(float(liste[sayac+1])-float(liste[sayac+2])))
			newlist.append(str(float(liste[sayac+1])-float(liste[sayac+2])))
			sayac+=2
		elif (sayac+1)<len(liste) and (sayac+2)<len(liste) and liste[sayac]=="/" and not (liste[sayac+1] in operand) and not (liste[sayac+2] in operand):
			print(str(float(liste[sayac+1])-float(liste[sayac+2])))
			newlist.append(str(float(liste[sayac+1])/float(liste[sayac+2])))
			sayac+=2
		else:
			print(liste[sayac])
			newlist.append(liste[sayac])
		sayac+=1
	if (sayac)<len(liste):
		newlist.append(liste[sayac])
	liste=newlist
	kontrol=0
	sayac = 0
	newlist=[]


print("TAMAMLANMIS ISLEM : ")
print(liste[0])