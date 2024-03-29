#Help https://youtu.be/H37f_x4wAC0
def octant_longest_subsequence_count_with_range():
###Code
    #importing libraries
    import pandas as pd

    #for data preprocessing read all data
    try:
        data = pd.read_excel("input_octant_longest_subsequence_with_range.xlsx")

    
    
        cnt=0
        o_1=o_2=o_3=o_4=o_5=o_6=o_7=o_8=0

        d_2 = data.U
        d_3 = data.V
        d_4 = data.W
        time = data.Time
        d1= {'+++': '+1', "++-": '-1', "-++": '+2', "-+-": '-2',
            "--+": '+3', "---": '-3', "+-+": '+4', "+--": '-4'}
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

        w1 = [i-acc for i in data['W']]     
        v1 = [i-final for i in data['V']]
        u1 = [i-intial for i in data['U']]

        pg = pd.DataFrame(makedata)

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
        f1=[]
        f2=[]
        f3=[]
        f4=[]
        f5=[]
        f6=[]
        f7=[]
        f8=[]
        t1=[]
        t2=[]
        t3=[]
        t4=[]
        t5=[]
        t6=[]
        t7=[]
        t8=[]
        for i in range(len(a1)):
            if(i==0):
                v=1
            elif(Octant[i]==Octant[i-1]):
                v+=1
            else:
                if(Octant[i-1]=='+1' and u1<=v):
                    if(u1<v):
                        u11=1
                    else:
                        u11+=1
                    u1=v
                elif(Octant[i-1]=='-1' and u2<=v):
                    if(u2<v):
                        u22=1
                    else:
                        u22+=1
                    u2=v
                elif(Octant[i-1]=='+2' and u3<=v):
                    if(u3<v):
                        u33=1
                    else:
                        u33+=1
                    u3=v
                elif(Octant[i-1]=='-2' and u4<=v):
                    if(u4<v):
                        u44=1
                    else:
                        u44+=1
                    u4=v
                elif(Octant[i-1]=='+3' and u5<=v):
                    if(u5<v):
                        u55=1
                    else:
                        u55+=1
                    u5=v
                elif(Octant[i-1]=='-3' and u6<=v):
                    if(u6<v):
                        u66=1
                    else:
                        u66+=1
                    u6=v
                elif(Octant[i-1]=='+4' and u7<=v):
                    if(u7<v):
                        u77=1
                    else:
                        u77+=1
                    u7=v
                elif(Octant[i-1]=='-4' and u8<=v):
                    if(u8<v):
                        u88=1
                    else:
                        u88+=1
                    u8=v
                v=1
        if(Octant[len(a1)-1]=='+1' and u1<=v):
            if(u1<v):
                u11=1
            else:
                u11+=1
            u1=v
        elif(Octant[len(a1)-1]=='-1' and u2<=v):
            if(u2<v):
                u22=1
            else:
                u22+=1
            u2=v
        elif(Octant[len(a1)-1]=='+2' and u3<=v):
            if(u3<v):
                u33=1
            else:
                u33+=1
            u3=v
        elif(Octant[len(a1)-1]=='-2' and u4<=v):
            if(u4<v):
                u44=1
            else:
                u44+=1
            u4=v
        elif(Octant[len(a1)-1]=='+3' and u5<=v):
            if(u5<v):
                u55=1
            else:
                u55+=1
            u5=v
        elif(Octant[len(a1)-1]=='-3' and u6<=v):
            if(u6<v):
                u66=1
            else:
                u66+=1
            u6=v
        elif(Octant[len(a1)-1]=='+4' and u7<=v):
            if(u7<v):
                u77=1
            else:
                u77+=1
            u7=v
        elif(Octant[len(a1)-1]=='-4' and u8<=v):
            if(u8<v):
                u88=1
            else:
                u88+=1
            u8=v
        e=0
        for i in range(len(a1)):
            if(i==0):
                e=1
            elif(Octant[i]==Octant[i-1]):
                e+=1
            elif(Octant[i]!=Octant[i-1]):
                if(Octant[i-1]=='+1' and e==u1):
                    f1.append(time[i-e])
                    t1.append(time[i-1])
                elif(Octant[i-1]=='-1' and e==u2):
                    f2.append(time[i-e])
                    t2.append(time[i-1])
                elif(Octant[i-1]=='+2' and e==u3):
                    f3.append(time[i-e])
                    t3.append(time[i-1])
                elif(Octant[i-1]=='-2' and e==u4):
                    f4.append(time[i-e])
                    t4.append(time[i-1])
                elif(Octant[i-1]=='+3' and e==u5):
                    f5.append(time[i-e])
                    t5.append(time[i-1])
                elif(Octant[i-1]=='-3' and e==u6):
                    f6.append(time[i-e])
                    t6.append(time[i-1])
                elif(Octant[i-1]=='+4' and e==u7):
                    f7.append(time[i-e])
                    t7.append(time[i-1])
                elif(Octant[i-1]=='-4' and e==u8):
                    f8.append(time[i-e])
                    t8.append(time[i-1])
                e=1
        if(Octant[len(a1)-1]=='+1' and e==u1):
            f1.append(time[len(a1)-e])
            t1.append(time[len(a1)-1])
        elif(Octant[len(a1)-1]=='-1' and e==u2):
            f2.append(time[len(a1)-e])
            t2.append(time[len(a1)-1])
        elif(Octant[len(a1)-1]=='+2' and e==u3):
            f3.append(time[len(a1)-e])
            t3.append(time[len(a1)-1])
        elif(Octant[len(a1)-1]=='-2' and e==u4):
            f4.append(time[len(a1)-e])
            t4.append(time[len(a1)-1])
        elif(Octant[len(a1)-1]=='+3' and e==u5):
            f5.append(time[len(a1)-e])
            t5.append(time[len(a1)-1])
        elif(Octant[len(a1)-1]=='-3' and e==u6):
            f6.append(time[len(a1)-e])
            t6.append(time[len(a1)-1])
        elif(Octant[len(a1)-1]=='+4' and e==u7):
            f7.append(time[len(a1)-e])
            t7.append(time[len(a1)-1])
        elif(Octant[len(a1)-1]=='-4' and e==u8):
            f8.append(time[len(a1)-e])
            t8.append(time[len(a1)-1])
        longest_subsequence = [u1,u2,u3,u4,u5,u6,u7,u8]
        cnt = [u11,u22,u33,u44,u55,u66,u77,u88]
        OctantId = ['+1','-1','+2','-2','+3','-3','+4','-4']
        sa = {"": [None]}
        saa = pd.DataFrame(sa)
        da = {"OctantID": OctantId, "Longest subsequence length": longest_subsequence, "Count": cnt}
        o=['+1']
        uu=[u1]
        uuu=[u11]
        db = {"Octant_ID": o, "Longest_subsequence_length": uu, "Count_": uuu}
        h1 = pd.DataFrame(da)
        h2 =pd.DataFrame(db)
        r = {"Octant_ID": "Time", "Longest_subsequence_length": "From", "Count_": "To"}
        h2 = h2.append(r, ignore_index=True)

        for i in range(8):
            if(i==0):
                for j in range(u11):
                    r_0 = {"Longest_subsequence_length": f1[j], "Count_": t1[j]}
                    h2 = h2.append(r_0, ignore_index=True)
            if(i==1):
                rr = {"Octant_ID": '-1', "Longest_subsequence_length": u2, "Count_": u22}
                h2 = h2.append(rr, ignore_index=True)
                r = {"Octant_ID": "Time", "Longest_subsequence_length": "From", "Count_": "To"}
                h2 = h2.append(r, ignore_index=True)
                for j in range(u22):
                    r_0 = {"Longest_subsequence_length": f2[j], "Count_": t2[j]}
                    h2 = h2.append(r_0, ignore_index=True)
            if(i==2):
                rr = {"Octant_ID": '+2', "Longest_subsequence_length": u3, "Count_": u33}
                h2 = h2.append(rr, ignore_index=True)                
                r = {"Octant_ID": "Time", "Longest_subsequence_length": "From", "Count_": "To"}
                h2 = h2.append(r, ignore_index=True)
                for j in range(u33):
                    r_0 = {"Longest_subsequence_length": f3[j], "Count_": t3[j]}
                    h2 = h2.append(r_0, ignore_index=True)
            if(i==3):
                rr = {"Octant_ID": '-2', "Longest_subsequence_length": u4, "Count_": u44}
                h2 = h2.append(rr, ignore_index=True)
                r = {"Octant_ID": "Time", "Longest_subsequence_length": "From", "Count_": "To"}
                h2 = h2.append(r, ignore_index=True)    
                for j in range(u44):
                    r_0 = {"Longest_subsequence_length": f4[j], "Count_": t4[j]}
                    h2 = h2.append(r_0, ignore_index=True)
            if(i==4):
                rr = {"Octant_ID": '+3', "Longest_subsequence_length": u5, "Count_": u55}
                h2 = h2.append(rr, ignore_index=True)
                r = {"Octant_ID": "Time", "Longest_subsequence_length": "From", "Count_": "To"}
                h2 = h2.append(r, ignore_index=True)
                for j in range(u55):
                    r_0 = {"Longest_subsequence_length": f5[j], "Count_": t5[j]}
                    h2 = h2.append(r_0, ignore_index=True)
            if(i==5):
                rr = {"Octant_ID": '-3', "Longest_subsequence_length": u6, "Count_": u66}
                h2 = h2.append(rr, ignore_index=True)
                r = {"Octant_ID": "Time", "Longest_subsequence_length": "From", "Count_": "To"}
                h2 = h2.append(r, ignore_index=True)
                for j in range(u66):
                    r_0 = {"Longest_subsequence_length": f6[j], "Count_": t6[j]}
                    h2 = h2.append(r_0, ignore_index=True)
            if(i==6):
                rr = {"Octant_ID": '+4', "Longest_subsequence_length": u7, "Count_": u77}
                h2 = h2.append(rr, ignore_index=True)
                r = {"Octant_ID": "Time", "Longest_subsequence_length": "From", "Count_": "To"}
                h2 = h2.append(r, ignore_index=True)
                for j in range(u77):
                    r_0 = {"Longest_subsequence_length": f7[j], "Count_": t7[j]}
                    h2 = h2.append(r_0, ignore_index=True)
            if(i==7):
                rr = {"Octant_ID": '-4', "Longest_subsequence_length": u8, "Count_": u88}
                h2 = h2.append(rr, ignore_index=True)
                r = {"Octant_ID": "Time", "Longest_subsequence_length": "From", "Count_": "To"}
                h2 = h2.append(r, ignore_index=True)
                for j in range(u88):
                    r_0 = {"Longest_subsequence_length": f8[j], "Count_": t8[j]}
                    h2 = h2.append(r_0, ignore_index=True)

        fra = [pg, saa, h1, saa, h2]


        ans = pd.concat(fra, axis=1)
        ans.to_excel("output_octant_longest_subsequence_with_range.xlsx", index=False)

    except:
        print("Something went wrong while opening the file or file is not found.")
        exit()
        


from platform import python_version
ver = python_version()

if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")


octant_longest_subsequence_count_with_range()