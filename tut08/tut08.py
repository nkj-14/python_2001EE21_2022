
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
