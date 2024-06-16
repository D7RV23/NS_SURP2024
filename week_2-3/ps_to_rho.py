"""
@author: Diego Gamarra

"""
#declaring libraries
import pickle
#acceses the pickle file with all the Neutron star data, if you dont have the file, or the adress is wrong then the program wont run
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
print ("p Local")
p_local = pickle["DS_CMF1_wcrust/"]['ps']
print (p_local)
print("")
print("")

#all the above is for both testing purposes, and to check if the pickle file exist, as none of this would work otherwise
p_target = float(input("Please Enter P value: "))

print("")
print("")


#will compare the current p_target value and then use it to the the ps local value, stored in the x variable
for x in range(len(p_local)-1):
#first case: when the p_targer is less that the first value of the p_local
    if p_target < p_local[0]:
        p_target = p_local[0]
        x = 0
        break
#second case: when the p_target is greater than the last value of the p_local    
    if p_target >= p_local[-1]:
        #have to do this as otherwise it would try to access a value that does not exist
        p_target = p_local[-1]
        x = len(p_local)-2
        break
#Deaufult case: when the p_target is between the parameters of p_target        
    if p_local[x] < p_target and p_local[x+1] > p_target:
       break
#print (p_local[x])
#
#will use interpolation to find P_target

print("rho_Local: ",rho_local[x],)
rho_target = rho_local[x] + (((rho_local[x+1] - rho_local[x]) / (p_local[x+1] - p_local[x])) * (p_target - p_local[x]))

print("rho_target: ", rho_target)

