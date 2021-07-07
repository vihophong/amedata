from __future__ import print_function
import struct
import numpy as np

file1 = open("mass_1.mas20.txt")
data1 = []
iline = 0
flagread = 0
flagreadfirst = 0
print("N-Z,N,Z,A,EL,O,Mass_excess_keV,D_Mass_excess_keV,Binding_enrgy_perA_keV,D_Binding_enrgy_perA_keV,Decay_mode,Qbeta_keV,D_Qbeta_keV,A,Atomic_mass_microu,D_Atomic_mass_microu,end")
while True:
	iline += 1
	line = file1.readline()
	if not line:
		break
	items = line.split()
	if (len(items)==0):
		continue
	if (line[0]=="1"):
		flagread += 1
	if (flagread<2):
		continue
	if (line[0]=="0"):
		flagreadfirst += 1
	if (flagreadfirst==0):
		continue
	firstitem = 0
	if line[0]=="0":
		firstitem = 1

	col6flag = 0
	try:
		val = float(items[firstitem+5])
	except ValueError:
		#print(items[firstitem+5])
		if items[firstitem+5][len(items[firstitem+5])-1]=="#":
			col6flag = 0
		else:
			col6flag = 1
	columnitems = []
	for i in range(firstitem,len(items)):
		if (col6flag==0 and i-firstitem==5):
			columnitems.append("na")
		columnitems.append(items[i])
		if items[i]=="*":
			columnitems.append("999999")
		#print items[i],
	#print("")
	for i in range(len(columnitems)):
		if (columnitems[i]=="*"):
			columnitems[i] = "999999"
		if (columnitems[i][len(columnitems[i])-1]=="#"):
			columnitems[i] = columnitems[i][:len(columnitems[i])-1]
	for i in range(len(columnitems)):
		print(columnitems[i],end=',')
	print("end")
	data1.append({"N-Z": int(columnitems[0]),"N": int(columnitems[1]),"Z": int(columnitems[2]),"A": int(columnitems[3]),"EL": str(columnitems[4]),
		"O": str(columnitems[5]),"M": float(columnitems[6]),"DM": float(columnitems[7]),"B": float(columnitems[8]),
		"DB": float(columnitems[9]), "Decay": str(columnitems[10]),"Qb": float(columnitems[11]),
		"DQb": float(columnitems[12]), "A2": int(columnitems[13]), "AM": float(columnitems[14]),"DAM": float(columnitems[15]) })

np.save("mass_1.mas20.npy",data1)


