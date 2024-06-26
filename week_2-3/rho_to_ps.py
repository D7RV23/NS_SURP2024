"""
@author Diego Gamarra
"""

import pickle


pickleContents = open ( r"C:\Users\17573\Documents\School\SURP-2024\week-2\eostable.pk", "rb" )

pickle = pickle.load(pickleContents)

print(pickle.keys())
print(pickle["DS_CMF1_wcrust/"].keys())
print(pickle["DS_CMF1_wcrust/"]['rhos'])
#pickle.("DS(0CMF)-1")

#prints the rho local values
print ("rhos Local")
rho_local = pickle["DS_CMF1_wcrust/"]['rhos']
print (rho_local) 
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
for x in range(len(rho_local)-1):
#first case: when the p_targer is less that the first value of the p_local
    if rho_target < rho_local[0]:
            rho_target = rho_local[0]
            break
#second case: when the p_target is greater than the last value of the p_local    
    if rho_target <= rho_local[-1]:
            #have to do this as otherwise it would try to access a value that does not exist
            rho_target = rho_local[-2]
            break
#Deafult case, When the rho target is between the given parameters needed
    if rho_local[x] < rho_target and rho_local[x+1] > rho_target:
            #local = x
            break
#print (p_local[x])
# i thougth that i would need to make a different value that would take the x value, however that wont be needed as all
#
#
#will use interpolation to find P_target
#Equation used:  
print("p_Local: ",p_local[x])
p_target = p_local[x] + (((p_local[x+1] - p_local[x]) / (rho_local[x+1] - rho_local[x])) * (rho_target - rho_local[x]))

print("P_target: ", p_target) 
