

from datetime import datetime
start_time = datetime.now()

#Help https://youtu.be/H37f_x4wAC0
def octant_longest_subsequence_count():
###Code
    #importing libraries
    import pandas as pd


    #for data preprocessing read all data
    try:
        data = pd.read_excel("input_octant_longest_subsequence.xlsx")

    
        cnt=0
        o_1=o_2=o_3=o_4=o_5=o_6=o_7=o_8=0

        d_2 = data.U
        d_3 = data.V
        d_4 = data.W
        d1= {'+++': +1, "++-": -1, "-++": +2, "-+-": -2,
            "--+": +3, "---": -3, "+-+": +4, "+--": -4}
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
   
        
        #print("o_1 = ", o_1)
        #print("o_2 = ", o_2)
        #print("o_3 = ", o_3)
        #print("o_4 = ", o_4)
        #print("o_5 = ", o_5)
        #print("o_6 = ", o_6)
        #print("o_7 = ", o_7)
        #print("o_8 = ", o_8)

        intial = data['U'].mean()
        final = data['V'].mean()
        acc = data['W'].mean()    

    except:
        print("Something went wrong while opening the file or file is not found.")
        exit()


from platform import python_version
ver = python_version()

if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")


octant_longest_subsequence_count()






#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))