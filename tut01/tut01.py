#importing libraries
import pandas as pd

#for data preprocessing read all data
data = pd.read_csv("octant_input.csv")

from platform import python_version
ver = python_version()

if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")

cnt=0
o_1=o_2=o_3=o_4=o_5=o_6=o_7=o_8=0

d_2 = data.U
d_3 = data.V
d_4 = data.W
d1= {'+++': "+1", "++-": "-1", "-++": "+2", "-+-": "-2",
    "--+": "+3", "---": "-3", "+-+": "+4", "+--": "-4"}
Octant = []
for r in range(len(d_2)):
    if d_2[r]>0  and d_3[r]>0 and d_4[r]>0:
        o_1=o_1+1
    if d_2[r]>0  and d_3[r]>0 and d_4[r]<0:
        o_2=o_2+1
    if d_2[r]<0  and d_3[r]>0 and d_4[r]>0:
        o_3=o_3+1
    if d_2[r]<0  and d_3[r]>0 and d_4[r]<0:
        o_4=o_4+1
    if d_2[r]<0  and d_3[r]<0 and d_4[r]>0:
        o_5=o_5+1
    if d_2[r]<0  and d_3[r]<0 and d_4[r]<0:
        o_6=o_6+1
    if d_2[r]>0  and d_3[r]<0 and d_4[r]>0:
        o_7=o_7+1
    if d_2[r]>0  and d_3[r]<0 and d_4[r]<0:
        o_8=o_8+1
   
        
print("o_1 = ", o_1)
print("o_2 = ", o_2)
print("o_3 = ", o_3)
print("o_4 = ", o_4)
print("o_5 = ", o_5)
print("o_6 = ", o_6)
print("o_7 = ", o_7)
print("o_8 = ", o_8)

intial = data['U'].mean()
final = data['V'].mean()
acc = data['W'].mean()



def octact_identification(mod=5000):
###Code


from platform import python_version
ver = python_version()

if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")

mod=5000
octact_identification(mod)