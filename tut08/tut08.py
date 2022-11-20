
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
