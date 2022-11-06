

from datetime import date,datetime,timedelta
from tracemalloc import start
start_time = datetime.now()

def attendance_report():
###Code

    #importing libraries
    import pandas as pd

    try:
        d1 = pd.read_csv("input_registered_students.csv")
        d2 = pd.read_csv("input_attendance.csv")

        roll = d1["Roll No"]
        name = d1["Name"]
        timestamp = d2["Timestamp"]
        attendance = d2["Attendance"]
        attendance_roll = []
        dates = []
        dat = {}
        din = {}

        for i in range(len(timestamp)):
            attendance_roll.append(attendance[i][0:8])

        cc = 0
        for i in range(len(timestamp[0])):
            if(timestamp[0][i]=='/'):
                cc=1
                break
            elif(timestamp[0][i]=='-'):
                cc=2
                break
        if(cc==1):
            f1 = "%d/%m/%Y %H:%M"
            d = datetime.strptime(timestamp[0], f1)
            dd = d.timetuple()
            start_date = date(dd[0], dd[1], dd[2])
            ee=0
            for i in range(len(timestamp[len(timestamp)-1])):
                if(timestamp[0][i]=='/'):
                    ee=1
                    break
                elif(timestamp[0][i]=='-'):
                    ee=2
                    break
            if(ee==1):
                f2 = "%d/%m/%Y %H:%M"
                t = datetime.strptime(timestamp[len(timestamp)-1], f2)
                tt = t.timetuple()
                end_date = date(tt[0], tt[1], tt[2])
                delta = timedelta(days=1)
                while start_date <= end_date:
                    s=start_date.timetuple()
                    if(s[6]==0 or s[6]==3):
                        dates.append(start_date)
                        dat[start_date] = []
                        din[start_date] = []
                    start_date += delta

            elif(ee==2):
                f2 = "%d-%m-%Y %H:%M"
                t = datetime.strptime(timestamp[len(timestamp)-1], f2)
                tt = t.timetuple()
                end_date = date(tt[0], tt[1], tt[2])
                delta = timedelta(days=1)
                while start_date <= end_date:
                    s=start_date.timetuple()
                    if(s[6]==0 or s[6]==3):
                        dates.append(start_date)
                        dat[start_date] = []
                        din[start_date] = []
                    start_date += delta

        elif(cc==2):
            f1 = "%d-%m-%Y %H:%M"
            t = datetime.strptime(timestamp[0], f1)
            tt = t.timetuple()
            start_date = date(tt[0], tt[1], tt[2])
            ee=0
            for i in range(len(timestamp[len(timestamp)-1])):
                if(timestamp[0][i]=='/'):
                    ee=1
                    break
                elif(timestamp[0][i]=='-'):
                    ee=2
                    break
            if(ee==1):
                f2 = "%d/%m/%Y %H:%M"
                d = datetime.strptime(timestamp[len(timestamp)-1], f2)
                dd = d.timetuple()
                end_date = date(dd[0], dd[1], dd[2])
                delta = timedelta(days=1)
                while start_date <= end_date:
                    s=start_date.timetuple()
                    if(s[6]==0 or s[6]==3):
                        dates.append(start_date)
                        dat[start_date] = []
                        din[start_date] = []
                    start_date += delta

            elif(ee==2):
                f2 = "%d-%m-%Y %H:%M"
                d = datetime.strptime(timestamp[len(timestamp)-1], f2)
                dd = d.timetuple()
                end_date = date(dd[0], dd[1], dd[2])
                delta = timedelta(days=1)
                while start_date <= end_date:
                    s=start_date.timetuple()
                    if(s[6]==0 or s[6]==3):
                        dates.append(start_date)
                        dat[start_date] = []
                        din[start_date] = []
                    start_date += delta

    
        for i in range(len(timestamp)):
            
            c = 0
            for j in range(len(timestamp[i])):
                if(timestamp[i][j]=='/'):
                    c=1
                    break
                elif(timestamp[i][j]=='-'):
                    c=2
                    break
            if(c==1):
                f3 = "%d/%m/%Y %H:%M"
                do = datetime.strptime(timestamp[i], f3)
                doo = do.timetuple()
                star = date(doo[0], doo[1], doo[2])
                if(star in dates):
                    if(do.hour == 14 or (do.hour == 15 and do.minute==0 and do.microsecond==0)):
                        dat[star].append(attendance_roll[i])
                    else:
                        din[star].append(attendance_roll[i])
        
            elif(c==2):
                f3 = "%d-%m-%Y %H:%M"
                do = datetime.strptime(timestamp[i], f3)
                doo = do.timetuple()
                star = date(doo[0], doo[1], doo[2])
                if(star in dates):
                    if(do.hour == 14 or (do.hour == 15 and do.minute==0 and do.microsecond==0)):
                        dat[star].append(attendance_roll[i])
                    else:
                        din[star].append(attendance_roll[i])


    except:
        print("Something went wrong while opening the file or file is not found.")
        exit()

from platform import python_version
ver = python_version()

if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")


attendance_report()




#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
