

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


        #from tqdm.notebook import tqdm
        data
        o1=[intial]
        o2=[final]
        o3=[acc]

        # print("Octant ID", "1", "-1", "2", "-2", "3", "-3", "4", "-4")
        # print("Overall count", o_1, o_2, o_3, o_4, o_5, o_6, o_7, o_8)
        # d = [[]]
        for i in range(len(data['Time'])-1):
                o1.append(None)
                o2.append(None)
                o3.append(None)
        d=[["Overall count"],[o_1, o_2, o_3, o_4, o_5, o_6, o_7, o_8]]
        makedata = {"Time": data['Time'], "U":data["U"], "V":data["V"],
                        "W":data["W"], "U Avg":o1,"V Avg": o2, "W Avg": o3}


        j = r = 0

        if r==0:
            o_1=o_2=o_3=o_4=o_5=o_6=o_7=o_8=0
        if d_2[r]>0  and d_3[r]>0 and d_4[r]>0:
            o_1=o_1+1
        elif d_2[r]>0  and d_3[r]>0 and d_4[r]<0:
            o_2=o_2+1
        elif d_2[r]<0  and d_3[r]>0 and d_4[r]>0:
            o_3=o_3+1
        elif d_2[r]<0  and d_3[r]>0 and d_4[r]<0:
            o_4=o_4+1
        elif d_2[r]<0  and d_3[r]<0 and d_4[r]>0:
            o_5=o_5+1
        elif d_2[r]<0  and d_3[r]<0 and d_4[r]<0:
            o_6=o_6+1
        elif d_2[r]>0  and d_3[r]<0 and d_4[r]>0:
            o_7=o_7+1
        elif d_2[r]>0  and d_3[r]<0 and d_4[r]<0:
            o_8=o_8+1
        # if r%mod==mod-1:
        #         # print(r-(mod-1),'-',r, o_1, o_2, o_3, o_4, o_5, o_6, o_7, o_8)

            
        w1 = [i-acc for i in data['W']]     
        v1 = [i-final for i in data['V']]
        u1 = [i-intial for i in data['U']]

        pg = pd.DataFrame(makedata)
            # make new columns of three variables
        pg["U'=U-Uavg"] = u1
        pg["V'=V-Vavg"] = v1
        pg["W'=W-Wavg"] = w1

        Octant = []

        b1 = pg["V'=V-Vavg"].to_list()
        c1 = pg["W'=W-Wavg"].to_list()
        a1 = pg["U'=U-Uavg"].to_list()
        for i in range(len(a1)):
                s = ""
                if (a1[i] < 0):
                    s += '-'
                else:
                    s += '+'
                if (b1[i] < 0):
                    s += '-'
                else:
                    s += '+'
                if (c1[i] < 0):
                    s += '-'
                else:
                    s += '+'
                Octant.append(d1[s])

        pg["Octant"] = Octant
        v=u1=u2=u3=u4=u5=u6=u7=u8=u11=u22=u33=u44=u55=u66=u77=u88=0
        for i in range(len(a1)):
            if(i==0):
                v=1
            elif(Octant[i]==Octant[i-1]):
                v+=1
            else:
                if(Octant[i-1]==+1 and u1<=v):
                    if(u1<v):
                        u11=1
                    else:
                        u11+=1
                    u1=v
                elif(Octant[i-1]==-1 and u2<=v):
                    if(u2<v):
                        u22=1
                    else:
                        u22+=1
                    u2=v
                elif(Octant[i-1]==+2 and u3<=v):
                    if(u3<v):
                        u33=1
                    else:
                        u33+=1
                    u3=v
                elif(Octant[i-1]==-2 and u4<=v):
                    if(u4<v):
                        u44=1
                    else:
                        u44+=1
                    u4=v
                elif(Octant[i-1]==+3 and u5<=v):
                    if(u5<v):
                        u55=1
                    else:
                        u55+=1
                    u5=v
                elif(Octant[i-1]==-3 and u6<=v):
                    if(u6<v):
                        u66=1
                    else:
                        u66+=1
                    u6=v
                elif(Octant[i-1]==+4 and u7<=v):
                    if(u7<v):
                        u77=1
                    else:
                        u77+=1
                    u7=v
                elif(Octant[i-1]==-4 and u8<=v):
                    if(u8<v):
                        u88=1
                    else:
                        u88+=1
                    u8=v
                v=1
        if(Octant[len(a1)-1]==+1 and u1<=v):
            if(u1<v):
                u11=1
            else:
                u11+=1
            u1=v
        elif(Octant[len(a1)-1]==-1 and u2<=v):
            if(u2<v):
                u22=1
            else:
                u22+=1
            u2=v
        elif(Octant[len(a1)-1]==+2 and u3<=v):
            if(u3<v):
                u33=1
            else:
                u33+=1
            u3=v
        elif(Octant[len(a1)-1]==-2 and u4<=v):
            if(u4<v):
                u44=1
            else:
                u44+=1
            u4=v
        elif(Octant[len(a1)-1]==+3 and u5<=v):
            if(u5<v):
                u55=1
            else:
                u55+=1
            u5=v
        elif(Octant[len(a1)-1]==-3 and u6<=v):
            if(u6<v):
                u66=1
            else:
                u66+=1
            u6=v
        elif(Octant[len(a1)-1]==+4 and u7<=v):
            if(u7<v):
                u77=1
            else:
                u77+=1
            u7=v
        elif(Octant[len(a1)-1]==-4 and u8<=v):
            if(u8<v):
                u88=1
            else:
                u88+=1
            u8=v    

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