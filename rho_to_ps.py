import pickle



pickleContents = open ( r"C:\Users\17573\Desktop\School\SURP-2024\eostable.pk", "rb" )

pickle = pickle.load(pickleContents)

print(pickle.keys())
print(pickle["DS_CMF1_wcrust/"].keys())
print(pickle["DS_CMF1_wcrust/"]['rhos'])
#pickle.("DS(0CMF)-1")

#prints the rho local values
print ("rhos Local")
rhos_local = pickle["DS_CMF1_wcrust/"]['rhos']
print (rhos_local)
print("")
print("")


#print the ps local values
print ("ps Local")
p_local = pickle["DS_CMF1_wcrust/"]['ps']
print (p_local)
print("")
print("")

rho_target = float(input("Please Enter the Rho Target: "))
#for debug purposes
#print (x)
print("")
print("")

#will compare the current rho_target value and then use it to the the ps local value, stored in the x variable
for x in range(len(rhos_local)-1):
    if rhos_local[x] < rho_target and rhos_local[x+1] > rho_target:
        local = x
        break
#print (p_local[x])

#will use interpolation to find P_target
#Equation used:  
print("p_Local: ",p_local[x])
p_target = p_local[x] + (((p_local[x+1] - p_local[x]) / (rhos_local[x+1] - rhos_local[x])) * (rho_target - rhos_local[x]))

print("P_target: ", p_target) 
