def octant_transition_count(mod=5000):
###Code
    #importing libraries
    import pandas as pd

    #for data preprocessing read all data
    try:
        data = pd.read_excel("input_octant_transition_identify.xlsx")

    
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

        if r%mod==0:
            o_1=o_2=o_3=o_4=o_5=o_6=o_7=o_8=0
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
        if d_2[r]>0  and d_3[r]>0 and d_4[r]>0:
            o_1=o_1+1
        elif d_2[r]>0  and d_3[r]>0 and d_4[r]<0:
            o_2=o_2+1
        elif d_2[r]<0  and d_3[r]>0 and d_4[r]>0:
            o_3=o_3+1
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
        da = {"": [None], "OctantID": "Overall Count", 1: [Octant.count(+1)], -1: [Octant.count(-1)], 2: [Octant.count(+2)], -2: [Octant.count(-2)],
                    3: [Octant.count(+3)], -3: [Octant.count(-3)], 4: [Octant.count(+4)], -4: [Octant.count(-4)]}
        if d_2[r]>0  and d_3[r]>0 and d_4[r]>0:
            o_1=o_1+1
        elif d_2[r]>0  and d_3[r]>0 and d_4[r]<0:
            o_2=o_2+1
        elif d_2[r]<0  and d_3[r]>0 and d_4[r]>0:
            o_3=o_3+1
        h1= pd.DataFrame(da)
        t1 = mod
        new_row2 = {'': "User Input", "OctantID": "Mod"+" "+str(t1)}
        h1 = h1.append(new_row2, ignore_index=True)
        l=len(data['Time'])
        for i in range(0, l, t1):
                x = str(i)+"-"+str(i+t1-1)

                k = {"OctantID": x, 1: Octant[i:i+t1].count(+1), -1: Octant[i:i+t1].count(-1), 2: Octant[i:i+t1].count(+2),
                    -2: Octant[i:i+t1].count(-2), 3: Octant[i:i+t1].count(+3), -3: Octant[i:i+t1].count(-3),
                    4: Octant[i:i+t1].count(+4), -4: Octant[i:i+t1].count(-4)}
                h1 = h1.append(k, ignore_index=True)
        
        blank_row = {'':'', "OctantID":''}
        h1 = h1.append(blank_row, ignore_index=True)
        h1 = h1.append(blank_row, ignore_index=True)
        rowa = {"OctantID":"Overall Transition Count"}
        h1 = h1.append(rowa, ignore_index=True)
        row_to = {"OctantID":'', 1:"To"}
        h1 = h1.append(row_to, ignore_index=True)
        row_1 = {"OctantID":"Count", 1:1,-1:-1, 2:2,-2:-2, 3:3,-3:-3, 4:4,-4:-4}
        h1 = h1.append(row_1, ignore_index=True)

        transition_1 = []
        transition_11 = []
        transition_2 = []
        transition_22 = []
        transition_3 = []
        transition_33 = []
        transition_4 = []
        transition_44 = []

        for i in range(0, (l-1), 1):
                if(Octant[i+1]==+1):
                    transition_1.append(Octant[i])
                elif(Octant[i+1]==-1):
                    transition_11.append(Octant[i])
                elif(Octant[i+1]==+2):
                    transition_2.append(Octant[i])
                elif(Octant[i+1]==-2):
                    transition_22.append(Octant[i])
                elif(Octant[i+1]==+3):
                    transition_3.append(Octant[i])
                elif(Octant[i+1]==-3):
                    transition_33.append(Octant[i])
                elif(Octant[i+1]==+4):
                    transition_4.append(Octant[i])
                elif(Octant[i+1]==-4):
                    transition_44.append(Octant[i])

        r_1 = {"": "From", "OctantID": 1, 1: transition_1.count(+1), -1: transition_11.count(+1), 2: transition_2.count(+1), -2: transition_22.count(+1),
                    3: transition_3.count(+1), -3: transition_33.count(+1), 4: transition_4.count(+1), -4: transition_44.count(+1)}
        h1 = h1.append(r_1, ignore_index=True)
        r_11 = {"OctantID": -1, 1: transition_1.count(-1), -1: transition_11.count(-1), 2: transition_2.count(-1), -2: transition_22.count(-1),
                    3: transition_3.count(-1), -3: transition_33.count(-1), 4: transition_4.count(-1), -4: transition_44.count(-1)}
        r_2 = {"OctantID": 2, 1: transition_1.count(+2), -1: transition_11.count(+2), 2: transition_2.count(+2), -2: transition_22.count(+2),
                    3: transition_3.count(+2), -3: transition_33.count(+2), 4: transition_4.count(+2), -4: transition_44.count(+2)}
        r_22 = {"OctantID": -2, 1: transition_1.count(-2), -1: transition_11.count(-2), 2: transition_2.count(-2), -2: transition_22.count(-2),
                    3: transition_3.count(-2), -3: transition_33.count(-2), 4: transition_4.count(-2), -4: transition_44.count(-2)}
        r_3 = {"OctantID": 3, 1: transition_1.count(+3), -1: transition_11.count(+3), 2: transition_2.count(+3), -2: transition_22.count(+3),
                    3: transition_3.count(+3), -3: transition_33.count(+3), 4: transition_4.count(+3), -4: transition_44.count(+3)}
        r_33 = {"OctantID": -3, 1: transition_1.count(-3), -1: transition_11.count(-3), 2: transition_2.count(-3), -2: transition_22.count(-3),
                    3: transition_3.count(-3), -3: transition_33.count(-3), 4: transition_4.count(-3), -4: transition_44.count(-3)}
        r_4 = {"OctantID": 4, 1: transition_1.count(+4), -1: transition_11.count(+4), 2: transition_2.count(+4), -2: transition_22.count(+4),
                    3: transition_3.count(+4), -3: transition_33.count(+4), 4: transition_4.count(+4), -4: transition_44.count(+4)}
        r_44 = {"OctantID": -4, 1: transition_1.count(-4), -1: transition_11.count(-4), 2: transition_2.count(-4), -2: transition_22.count(-4),
                    3: transition_3.count(-4), -3: transition_33.count(-4), 4: transition_4.count(-4), -4: transition_44.count(-4)}
        h1 = h1.append(r_11, ignore_index=True)
        h1 = h1.append(r_2, ignore_index=True)
        h1 = h1.append(r_22, ignore_index=True)
        h1 = h1.append(r_3, ignore_index=True)
        h1 = h1.append(r_33, ignore_index=True)
        h1 = h1.append(r_4, ignore_index=True)
        h1 = h1.append(r_44, ignore_index=True)

        
        for j in range(0, l, t1):
                blank_row = {'':'', "OctantID":''}
                h1 = h1.append(blank_row, ignore_index=True)
                h1 = h1.append(blank_row, ignore_index=True)
                rowa = {"OctantID":"Mod Transition Count"}
                x = str(j)+"-"+str(j+t1)
                h1 = h1.append(rowa, ignore_index=True)
                row_to = {"OctantID":x, 1:"To"}
                h1 = h1.append(row_to, ignore_index=True)
                row_1 = {"OctantID":"Count", 1:1,-1:-1, 2:2,-2:-2, 3:3,-3:-3, 4:4,-4:-4}
                h1 = h1.append(row_1, ignore_index=True)

                transition_01 = []
                transition_011 = []
                transition_02 = []
                transition_022 = []
                transition_03 = []
                transition_033 = []
                transition_04 = []
                transition_044 = []

                for i in range(j, (j+t1), 1):
                    if((i)<(l-1)):
                        if(Octant[i+1]==+1):
                            transition_01.append(Octant[i])
                        elif(Octant[i+1]==-1):
                            transition_011.append(Octant[i])
                        elif(Octant[i+1]==+2):
                            transition_02.append(Octant[i])
                        elif(Octant[i+1]==-2):
                            transition_022.append(Octant[i])
                        elif(Octant[i+1]==+3):
                            transition_03.append(Octant[i])
                        elif(Octant[i+1]==-3):
                            transition_033.append(Octant[i])
                        elif(Octant[i+1]==+4):
                            transition_04.append(Octant[i])
                        elif(Octant[i+1]==-4):
                            transition_044.append(Octant[i])

                r_01 = {"": "From", "OctantID": 1, 1: transition_01.count(+1), -1: transition_011.count(+1), 2: transition_02.count(+1), -2: transition_022.count(+1),
                            3: transition_03.count(+1), -3: transition_033.count(+1), 4: transition_04.count(+1), -4: transition_044.count(+1)}
                h1 = h1.append(r_01, ignore_index=True)
                r_011 = {"OctantID": -1, 1: transition_01.count(-1), -1: transition_011.count(-1), 2: transition_02.count(-1), -2: transition_022.count(-1),
                            3: transition_03.count(-1), -3: transition_033.count(-1), 4: transition_04.count(-1), -4: transition_044.count(-1)}
                r_02 = {"OctantID": 2, 1: transition_01.count(+2), -1: transition_011.count(+2), 2: transition_02.count(+2), -2: transition_022.count(+2),
                            3: transition_03.count(+2), -3: transition_033.count(+2), 4: transition_04.count(+2), -4: transition_044.count(+2)}
                r_022 = {"OctantID": -2, 1: transition_01.count(-2), -1: transition_011.count(-2), 2: transition_02.count(-2), -2: transition_022.count(-2),
                            3: transition_03.count(-2), -3: transition_033.count(-2), 4: transition_04.count(-2), -4: transition_044.count(-2)}
                r_03 = {"OctantID": 3, 1: transition_01.count(+3), -1: transition_011.count(+3), 2: transition_02.count(+3), -2: transition_022.count(+3),
                            3: transition_03.count(+3), -3: transition_033.count(+3), 4: transition_04.count(+3), -4: transition_044.count(+3)}
                r_033 = {"OctantID": -3, 1: transition_01.count(-3), -1: transition_011.count(-3), 2: transition_02.count(-3), -2: transition_022.count(-3),
                            3: transition_03.count(-3), -3: transition_033.count(-3), 4: transition_04.count(-3), -4: transition_044.count(-3)}
                r_04 = {"OctantID": 4, 1: transition_01.count(+4), -1: transition_011.count(+4), 2: transition_02.count(+4), -2: transition_022.count(+4),
                            3: transition_03.count(+4), -3: transition_033.count(+4), 4: transition_04.count(+4), -4: transition_044.count(+4)}
                r_044 = {"OctantID": -4, 1: transition_01.count(-4), -1: transition_011.count(-4), 2: transition_02.count(-4), -2: transition_022.count(-4),
                            3: transition_03.count(-4), -3: transition_033.count(-4), 4: transition_04.count(-4), -4: transition_044.count(-4)}
                h1 = h1.append(r_011, ignore_index=True)
                h1 = h1.append(r_02, ignore_index=True)
                h1 = h1.append(r_022, ignore_index=True)
                h1 = h1.append(r_03, ignore_index=True)
                h1 = h1.append(r_033, ignore_index=True)
                h1 = h1.append(r_04, ignore_index=True)
                h1 = h1.append(r_044, ignore_index=True)

        fra = [pg, h1]

        ans = pd.concat(fra, axis=1)
        ans.to_excel("output_octant_transition_identify.xlsx", index=False)


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
octant_transition_count(mod)