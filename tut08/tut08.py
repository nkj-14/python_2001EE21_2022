
from datetime import datetime
start_time = datetime.now()

#Help


def innings(team):
        
    import pandas as pd

    teampak = open(team, "r").read()

    pakteam = []

    for r in teampak.split('\n'):
        pakteam.append(r)
    
    line = []
    toline = []
    for i in range(0,len(pakteam),2):
        line.append(pakteam[i].split(','))
        toline.append(pakteam[i].split(','))
    
    batsman = []
    ballers = []
    ball = []
    balls = ['0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '2.1', '2.2', '2.3', '2.4', '2.5', '2.6', '3.1', '3.2', '3.3', '3.4', '3.5', '3.6', '4.1', '4.2', '4.3', '4.4', '4.5', '4.6', '5.1', '5.2', '5.3', '5.4', '5.5', '5.6']
    for i in range(len(line)):
        players = line[i][0].split(' to ')
        batsman.append(players[1])
        ballers.append(players[0].split(' ', 1)[1])
        ball.append(players[0].split(' ')[0])
    batsman = list(dict.fromkeys(batsman))
    ballers = list(dict.fromkeys(ballers))

    datapakbat = pd.DataFrame(0, batsman, [' ', 'R', 'B', '4s', '6s', 'SR'])
    datapakbat[' '] = "not out"

    datapakball = pd.DataFrame(0, ballers, ['O', 'M', 'R', 'W', 'NB', 'WD', 'ECO'])

    forballnum = pd.DataFrame(0, ballers, ['B'])
    
    extra = wide = score = noball = wicket = b = lb = p = count = 0
    fall = []

    for i in range(len(line)):
        ballnum = line[i][0].split(' ',1)[0]
        player = line[i][0].split(' to ')
        batname = player[1]
        ballname = player[0].split(' ',1)[1]

        line[i][1] = line[i][1].lower()
        if line[i][1] == ' wide':
            wide = wide+1
            score = score+1
            extra = extra+1
            if(ball[i] in balls):
                count+=1
            datapakball.loc[ballname, 'R'] = datapakball.loc[ballname, 'R']+1
            datapakball.loc[ballname, 'WD'] = datapakball.loc[ballname, 'WD']+1
        elif line[i][1] == ' 2 wides':
            wide = wide+2
            score = score+2
            extra=extra+2
            if(ball[i] in balls):
                count+=2
            datapakball.loc[ballname, 'R'] = datapakball.loc[ballname, 'R']+2
            datapakball.loc[ballname, 'WD'] = datapakball.loc[ballname, 'WD']+2
        elif line[i][1] == ' 3 wides':
            wide = wide+3
            score = score+3
            extra=extra+3
            if(ball[i] in balls):
                count+=3
            datapakball.loc[ballname, 'R'] = datapakball.loc[ballname, 'R']+3
            datapakball.loc[ballname, 'WD'] = datapakball.loc[ballname, 'WD']+3

        elif line[i][1] == ' no ball':
            noball = noball+1
            score = score+1
            extra=extra+1
            if(ball[i] in balls):
                count+=1
            datapakball.loc[ballname, 'R'] = datapakball.loc[ballname, 'R']+1
            datapakball.loc[ballname, 'NB'] = datapakball.loc[ballname, 'NB']+1


        elif line[i][1] == ' four' or line[i][1] == ' 4' or line[i][1] == ' 4 runs' or line[i][1] == ' 4 run':
            datapakball.loc[ballname, 'R'] = datapakball.loc[ballname, 'R']+4
            forballnum.loc[ballname, 'B'] = forballnum.loc[ballname, 'B'] + 1
            if(ball[i] in balls):
                count+=4
            datapakbat.loc[batname, 'R'] = datapakbat.loc[batname, 'R'] + 4
            datapakbat.loc[batname, '4s'] = datapakbat.loc[batname, '4s'] + 1
            datapakbat.loc[batname, 'B'] = datapakbat.loc[batname, 'B'] + 1
            score = score+4


        elif line[i][1] == ' six' or line[i][1] == ' 6' or line[i][1] == ' 6 runs' or line[i][1] == ' 6 run':
            datapakball.loc[ballname, 'R'] = datapakball.loc[ballname, 'R']+6
            forballnum.loc[ballname, 'B'] = forballnum.loc[ballname, 'B'] + 1
            if(ball[i] in balls):
                count+=6
            datapakbat.loc[batname, 'R'] = datapakbat.loc[batname, 'R'] + 6
            datapakbat.loc[batname, '6s'] = datapakbat.loc[batname, '6s'] + 1
            datapakbat.loc[batname, 'B'] = datapakbat.loc[batname, 'B'] + 1
            score = score+6

        elif line[i][1] == ' 1' or line[i][1] == ' 1 run':
            datapakball.loc[ballname, 'R'] = datapakball.loc[ballname, 'R']+1
            forballnum.loc[ballname, 'B'] = forballnum.loc[ballname, 'B'] + 1
            if(ball[i] in balls):
                count+=1
            datapakbat.loc[batname, 'R'] = datapakbat.loc[batname, 'R'] + 1
            datapakbat.loc[batname, 'B'] = datapakbat.loc[batname, 'B'] + 1
            score = score+1

        elif line[i][1] == ' 2' or line[i][1] == ' 2 run' or line[i][1] == ' 2 runs':
            datapakball.loc[ballname, 'R'] = datapakball.loc[ballname, 'R']+2
            forballnum.loc[ballname, 'B'] = forballnum.loc[ballname, 'B'] + 1
            if(ball[i] in balls):
                count+=2
            datapakbat.loc[batname, 'R'] = datapakbat.loc[batname, 'R'] + 2
            datapakbat.loc[batname, 'B'] = datapakbat.loc[batname, 'B'] + 1
            score = score+2

        elif line[i][1] == ' 3' or line[i][1] == ' 3 run' or line[i][1] == ' 3 runs':
            datapakball.loc[ballname, 'R'] = datapakball.loc[ballname, 'R']+3
            forballnum.loc[ballname, 'B'] = forballnum.loc[ballname, 'B'] + 1
            if(ball[i] in balls):
                count+=3
            datapakbat.loc[batname, 'R'] = datapakbat.loc[batname, 'R'] + 3
            datapakbat.loc[batname, 'B'] = datapakbat.loc[batname, 'B'] + 1
            score = score+3

        elif line[i][1] == ' 5' or line[i][1] == ' 5 run' or line[i][1] == ' 5 runs':
            datapakball.loc[ballname, 'R'] = datapakball.loc[ballname, 'R']+5
            forballnum.loc[ballname, 'B'] = forballnum.loc[ballname, 'B'] + 1
            if(ball[i] in balls):
                count+=5
            datapakbat.loc[batname, 'R'] = datapakbat.loc[batname, 'R'] + 5
            datapakbat.loc[batname, 'B'] = datapakbat.loc[batname, 'B'] + 1
            score = score+5

        elif line[i][1] == ' no' or line[i][1] == ' no run':
            forballnum.loc[ballname, 'B'] = forballnum.loc[ballname, 'B'] + 1

            datapakbat.loc[batname, 'B'] = datapakbat.loc[batname, 'B'] + 1

        elif line[i][1] == ' leg byes' or line[i][1] == ' leg bye' or line[i][1] == ' lb':
            forballnum.loc[ballname, 'B'] = forballnum.loc[ballname, 'B'] + 1

            datapakbat.loc[batname, 'B'] = datapakbat.loc[batname, 'B'] + 1
            line[i][2] = line[i][2].lower()
            if line[i][2] == ' 1' or line[i][2] == ' 1 run':
                lb = lb+1
                score=score+1
                extra=extra+1
                
                if(ball[i] in balls):
                    count+=1
            if line[i][2] == ' 2' or line[i][2] == ' 2 run' or line[i][2] == ' 2 runs':
                lb = lb+2
                score=score+2
                extra=extra+2
                if(ball[i] in balls):
                    count+=2
                
            if line[i][2] == ' 3' or line[i][2] == ' 3 run' or line[i][2] == ' 3 runs':
                lb = lb+3
                score=score+3
                extra=extra+3
                if(ball[i] in balls):
                    count+=3

            if line[i][2] == ' 4' or line[i][2] == ' 4 run' or line[i][2] == ' 4 runs' or line[i][2] == ' four':
                lb = lb+4
                score=score+4
                extra=extra+4
                if(ball[i] in balls):
                    count+=4
            
            if line[i][2] == ' 5' or line[i][2] == ' 5 run' or line[i][2] == ' 5 runs':
                lb = lb+5
                score=score+5
                extra=extra+5
                if(ball[i] in balls):
                    count+=5
                
            if line[i][2] == ' 6' or line[i][2] == ' 6 run' or line[i][2] == ' 6 runs' or line[i][2] == ' six':
                lb = lb+6
                score=score+6
                extra=extra+6
                if(ball[i] in balls):
                    count+=6
                
        elif line[i][1] == ' byes' or line[i][1] == ' bye':
            forballnum.loc[ballname, 'B'] = forballnum.loc[ballname, 'B'] + 1

            datapakbat.loc[batname, 'B'] = datapakbat.loc[batname, 'B'] + 1
            line[i][2] = line[i][2].lower()
            if line[i][2] == ' 1' or line[i][2] == ' 1 run':
                b = b+1
                score=score+1
                extra=extra+1
                if(ball[i] in balls):
                    count+=1
                
            if line[i][2] == ' 2' or line[i][2] == ' 2 run' or line[i][2] == ' 2 runs':
                b = b+2
                score=score+2
                extra=extra+2
                if(ball[i] in balls):
                    count+=2
                
            if line[i][2] == ' 3' or line[i][2] == ' 3 run' or line[i][2] == ' 3 runs':
                b = b+3
                score=score+3
                extra=extra+3
                if(ball[i] in balls):
                    count+=3

            if line[i][2] == ' 4' or line[i][2] == ' 4 run' or line[i][2] == ' 4 runs' or line[i][2] == ' four':
                b = b+4
                score=score+4
                extra=extra+4
                if(ball[i] in balls):
                    count+=4
            
            if line[i][2] == ' 5' or line[i][2] == ' 5 run' or line[i][2] == ' 5 runs':
                b = b+5
                score=score+5
                extra=extra+5
                if(ball[i] in balls):
                    count+=5
                
            if line[i][2] == ' 6' or line[i][2] == ' 6 run' or line[i][2] == ' 6 runs' or line[i][2] == ' six':
                b = b+6
                score=score+6
                extra=extra+6
                if(ball[i] in balls):
                    count+=6

        else:
            forballnum.loc[ballname, 'B'] = forballnum.loc[ballname, 'B'] + 1
            datapakbat.loc[batname, 'B'] = datapakbat.loc[batname, 'B'] + 1 
            ad = str(score) + '-' + str(wicket+1) + ' (' + batname + ', ' + ballnum + ')'
            fall.append(ad)
            cont = line[i][1].split('!')
            if(cont[0]==' out bowled'):
                datapakball.loc[ballname, 'W'] = datapakball.loc[ballname, 'W']+1
                datapakbat.loc[batname, ' '] = 'b ' + ballname
                wicket=wicket+1

            elif(cont[0] == ' run out'):
                datapakbat.loc[batname, ' '] = 'run out'
                wicket=wicket+1

            elif (cont[0] == ' out lbw'):
                datapakball.loc[ballname, 'W'] = datapakball.loc[ballname, 'W']+1
                datapakbat.loc[batname, ' '] = 'lbw b ' + ballname
                wicket=wicket+1

            else:
                datapakball.loc[ballname, 'W'] = datapakball.loc[ballname, 'W']+1
                datapakbat.loc[batname, ' '] = 'c ' + toline[i][1].split('!')[0].split(' by ')[-1] + ' b ' + ballname
                wicket=wicket+1

        datapakbat.loc[batname, 'SR'] = round((((datapakbat.loc[batname, 'R'])/(datapakbat.loc[batname, 'B']))*100),2)
        datapakball.loc[ballname, 'O'] = (int(forballnum.loc[ballname, 'B']/6))+((forballnum.loc[ballname, 'B']%6)/10)
        datapakball.loc[ballname, 'ECO'] = (str(round(datapakball.loc[ballname, 'R']/(forballnum.loc[ballname, 'B']/6),1))+'0')

    if(team == 'pak_inns1.txt'):
        print(f"{'Pakistan Innings' : <20}{str(score)+'-'+str(wicket)+'('+str(ball[len(ball)-1])+' Ov)' : >70}")
    else:
        print(f"{'India Innings' : <20}{str(score)+'-'+str(wicket)+'('+str(ball[len(ball)-1])+' Ov)' : >70}")
    print(f"{'Batter':<20}{' ':<40}{'R':^5}{'B':^5}{'4s':^5}{'6s':^5}{'SR':>10}")
    for i in range(len(batsman)):
        print(f"{batsman[i]:<20}{datapakbat.loc[batsman[i], ' ']:<40}{datapakbat.loc[batsman[i], 'R']:^5}{datapakbat.loc[batsman[i], 'B']:^5}{datapakbat.loc[batsman[i], '4s']:^5}{datapakbat.loc[batsman[i], '6s']:^5}{datapakbat.loc[batsman[i], 'SR']:>10}")
    print(f"{'Extras':<60}{str(extra)+' (b '+str(b)+', lb '+str(lb)+', w '+str(wide)+', nb '+str(noball)+', p '+str(p)+')': <30}")
    print(f"{'Total': <60}{str(score)+' ('+str(wicket)+' wkts, '+str(ball[len(ball)-1])+' Ov)':<30}")
    print(f"{'Fall of Wickets':<90}")
    lo=''
    for i in range(len(fall)):
        lo=lo+fall[i]
        if(i!=len(fall)-1):
            lo=lo+', '
    print(f"{lo}")
    print(f"{'Bowler':<50}{'O':^5}{'M':^5}{'R':^5}{'W':5}{'NB':^5}{'WD':^5}{'ECO':>10}")
    for i in range(len(ballers)):
        print(f"{ballers[i]:<50}{datapakball.loc[ballers[i], 'O']:^5}{datapakball.loc[ballers[i], 'M']:^5}{datapakball.loc[ballers[i], 'R']:^5}{datapakball.loc[ballers[i], 'W']:5}{datapakball.loc[ballers[i], 'NB']:^5}{datapakball.loc[ballers[i], 'WD']:^5}{datapakball.loc[ballers[i], 'ECO']:>10}")
        
    print(f"{'Powerplays':<30}{'Overs':^30}{'Runs':>30}")
    print(f"{'Mandatory':<30}{'0.1-6':^30}{count:>30}")

def scorecard():
	pass


###Code

from platform import python_version
ver = python_version()

if ver == "3.8.10":
	print("Correct Version Installed")
else:
	print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")


scorecard()






#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
