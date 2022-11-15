
from openpyxl import Workbook
from openpyxl.styles import Border, Side, PatternFill
from datetime import datetime
start_time = datetime.now()

#Help
def octant_analysis(mod=5000):
	pass

##Read all the excel files in a batch format from the input/ folder. Only xlsx to be allowed
##Save all the excel files in a the output/ folder. Only xlsx to be allowed
## output filename = input_filename[_octant_analysis_mod_5000].xlsx , ie, append _octant_analysis_mod_5000 to the original filename. 

###Code
	#importing libraries
	import pandas as pd
	import glob
	import os


	try:

		path = "input" 
		filenames = glob.glob(path + "\*.xlsx")

		for file in filenames:

			print(str(file)[5:])

			wb = Workbook()
			ws = wb.active
			#ws.title = "output"

			d = pd.read_excel(file)


			d_1 = d["T"]
			d_2 = d["U"]
			d_3 = d["V"]
			d_4 = d["W"]
			d_5= {"+++": 1, "++-": -1, "-++": 2, "-+-": -2,
        		"--+": 3, "---": -3, "+-+": 4, "+--": -4}
			
			ini = round(d["U"].mean(),3)
			mi = round(d["V"].mean(),3)
			las = round(d["W"].mean(),3)
			o1 = [ini]
			o2 = [mi]
			o3 = [las]
			
			for i in range(len(d["T"])-1):
				o1.append(None)
				o2.append(None)
				o3.append(None)
			
			u1 = [round(i-ini,3) for i in d["U"]]
			v1 = [round(i-mi,3) for i in d["V"]]
			w1 = [round(i-las,3) for i in d["W"]]
			
			Octant = []
			for i in range(len(u1)):
				s = ""
				if(u1[i]<0):
					s += "-"
				else:
					s += "+"
				if(v1[i]<0):
					s += "-"
				else:
					s += "+"
				if(w1[i]<0):
					s += "-"
				else:
					s += "+"
				Octant.append(d_5[s])
				
			col = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]
			text = ["T", "U", "V", "W", "U Avg", "V Avg", "W Avg", "U'=U-U Avg", "V'=V-V Avg", "W'=W-W Avg", "Octant"]
			ri = 2
			wh = [d_1, d_2, d_3, d_4, o1, o2, o3, u1, v1, w1, Octant]
			



			
	except:
	    print("Something went wrong while opening the file or file is not found.")
        


from platform import python_version
ver = python_version()

if ver == "3.8.10":
	print("Correct Version Installed")
else:
	print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")


mod=5000
octant_analysis(mod)






#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
