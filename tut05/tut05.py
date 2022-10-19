

from datetime import datetime
start_time = datetime.now()

#Help https://youtu.be/N6PBd4XdnEw
def octant_range_names(mod=5000):

    
    octant_name_id_mapping = {"1":"Internal outward interaction", "-1":"External outward interaction", "2":"External Ejection", "-2":"Internal Ejection", "3":"External inward interaction", "-3":"Internal inward interaction", "4":"Internal sweep", "-4":"External sweep"}

###Code

    #importing libraries
    import pandas as pd

    #for data preprocessing read all data
    try:
        data = pd.read_excel("octant_input.xlsx")

    
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
   
        intial = data['U'].mean()
        final = data['V'].mean()
        acc = data['W'].mean()

        data
        o1=[intial]
        o2=[final]
        o3=[acc]

        for i in range(len(data['Time'])-1):
            o1.append(None)
            o2.append(None)
            o3.append(None)
        d=[["Overall count"],[o_1, o_2, o_3, o_4, o_5, o_6, o_7, o_8]]
        makedata = {"Time": data['Time'], "U":data["U"], "V":data["V"],
                        "W":data["W"], "U Avg":o1,"V Avg": o2, "W Avg": o3}


        j = r = 0

        if r%mod==0:
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
        da = {"": [None], "OctantID": "Overall Count", 1: [Octant.count('+1')], -1: [Octant.count('-1')], 2: [Octant.count('+2')], -2: [Octant.count('-2')],
                    3: [Octant.count('+3')], -3: [Octant.count('-3')], 4: [Octant.count('+4')], -4: [Octant.count('-4')]}

        h1= pd.DataFrame(da)
        t1 = mod
        new_row2 = {'': "User Input", "OctantID": "Mod"+" "+str(t1)}
        h1 = h1.append(new_row2, ignore_index=True)
        l=len(data['Time'])
        for i in range(0, l, t1):
            if (i+t1-1 >= l):
                x = str(i)+"-"+str(l-1)
            else:
                x = str(i)+"-"+str(i+t1-1)

            k = {"OctantID": x, 1: Octant[i:i+t1].count('+1'), -1: Octant[i:i+t1].count('-1'), 2: Octant[i:i+t1].count('+2'),
                -2: Octant[i:i+t1].count('-2'), 3: Octant[i:i+t1].count('+3'), -3: Octant[i:i+t1].count('-3'),
                4: Octant[i:i+t1].count('+4'), -4: Octant[i:i+t1].count('-4')}
            h1 = h1.append(k, ignore_index=True)

    except:
        print("Something went wrong while opening the file or file is not found.")
        exit()

from platform import python_version
ver = python_version()

if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")


mod=5000 
octant_range_names(mod)



#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
