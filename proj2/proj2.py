
from datetime import datetime
start_time = datetime.now()

#Help
def proj_octant_gui():
	pass


###Code
	
	import streamlit as st
	import pandas as pd
	import os

	st.markdown("<h1 style='text-align: center; color: grey;'>CS384 - Python</h1>", unsafe_allow_html=True)
	
	st.markdown("<h2 style='text-align: center; color: black;'>Project 2</h2>", unsafe_allow_html=True)

	st.markdown("<h2 style='text-align: center; color: black;'></h2>", unsafe_allow_html=True)

	st.markdown("<h5 style='text-align: left; color: black;'>Upload the correct input excel file:</h5>", unsafe_allow_html=True)

	ref = 0
	input_11=None
	input_1=None
	if(input_11==None):
		input_1 = st.file_uploader("")
		print(input_1)

	st.markdown("<h3 style='text-align: center; color: black;'></h3>", unsafe_allow_html=True)

	st.markdown("<h4 style='text-align: center; color: black;'>OR</h4>", unsafe_allow_html=True)


	st.markdown("<h3 style='text-align: center; color: black;'></h3>", unsafe_allow_html=True)


	st.markdown("<h5 style='text-align: left; color: black;'>Enter the correct path to the folder for bulk conversion:</h5>", unsafe_allow_html=True)

	if(input_1==None):
		input_11 = st.text_input("")
		

	st.markdown("<h3 style='text-align: center; color: black;'></h3>", unsafe_allow_html=True)


	st.markdown("<h5 style='text-align: left; color: black;'>Enter the mod value:</h5>", unsafe_allow_html=True)
	input_2 = st.number_input('', min_value=1, step=1)
	#Adding buttons
	st.markdown("<h2 style='text-align: center; color: black;'></h2>", unsafe_allow_html=True)

	bt = st.button('Compute')

	if(bt and input_11!=None):
		st.write('Do you want to download the resultant files ?')
		nt = st.button('Download')
		octant_analysis(input_11, input_2)
		if(nt):
			st.write('Resultant files have been downloaded in the same input folder path.')
	elif(bt and input_1.name[-5:]==".xlsx"):
		octant_analysis_single(input_1, input_2)
	elif(bt and input_1.name[-5:]!=".xlsx"):
		st.write("Uploded file is not excel type file.")



def octant_analysis(path, mod=5000):
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
		filenames = glob.glob(path + "\*.xlsx" , recursive=True)

		for file in filenames:
			#import xlsxwriter
			#from io import BytesIO
			#output = BytesIO()

			wb = Workbook()
			ws = wb.active
			#ws.title = "output"
			#wb = xlsxwriter.Workbook(output, engine='xlsxwriter')
			#ws = workbook.add_worksheet()



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
			

			for i in range(len(col)):
				ws[f"{col[i]}{ri}"].value = text[i]
				for r in range(3,len(d_1)+3):
					ws[f"{col[i]}{r}"].value = wh[i][r-3]
			c= "M"
			ws[f"{c}{4}"].value = "Mod " + str(mod)

			c= "N"
			ws[f"{c}{1}"].value = "Overall Octant Count"

			thin = Side(border_style="thin", color="000000")

			co = ["N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "AA", "AB", "AC", "AD", "AE", "AF"]
			tex = ["Octant ID", "+1", "-1", "+2", "-2", "+3", "-3", "+4", "-4", "Rank Octant 1", "Rank Octant -1", "Rank Octant 2", "Rank Octant -2", "Rank Octant 3", "Rank Octant -3", "Rank Octant 4", "Rank Octant -4", "Rank1 Octant ID", "Rank1 Octant Name"]

			for i in range(len(co)):
				ws[f"{co[i]}{3}"].value = tex[i]
				ws[f"{co[i]}{3}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)

			for p in range(len(co)):

				ws[f"{co[p]}{4}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
				OctantName = ["Internal outward interaction", "External outward interaction", "External Ejection", "Internal Ejection", "External inward interaction", "Internal inward interaction", "Internal sweep", "External sweep"]
				rr = [Octant.count(1), Octant.count(-1), Octant.count(2), Octant.count(-2), Octant.count(3), Octant.count(-3), Octant.count(4), Octant.count(-4)]
				rrr = [Octant.count(1), Octant.count(-1), Octant.count(2), Octant.count(-2), Octant.count(3), Octant.count(-3), Octant.count(4), Octant.count(-4)]
				rrr.sort(reverse=True)
				r1=r2=r3=r4=r5=r6=r7=r8=c=0
				for i in range(8):
					c=0
					for j in range(8):
						if(rr[i]==rrr[j]):
							if(j==0):
								if(i==0):
									ro=1
								elif(i==1):
									ro=-1
								elif(i==2):
									ro=2
								elif(i==3):
									ro=-2
								elif(i==4):
									ro=3
								elif(i==5):
									ro=-3
								elif(i==6):
									ro=4
								elif(i==7):
									ro=-4
								rn=OctantName[i]
							if(i==0):
								r1=(j+1)
							elif(i==1):
								r2=(j+1)
							elif(i==2):
								r3=(j+1)
							elif(i==3):
								r4=(j+1)
							elif(i==4):
								r5=(j+1)
							elif(i==5):
								r6=(j+1)
							elif(i==6):
								r7=(j+1)
							elif(i==7):
								r8=(j+1)
							c=1
						if(c==1):
							break
				if(co[p]=="N"):
					ws[f"{co[p]}{4}"].value = "Overall Count"
				elif(co[p]=="O"):
					ws[f"{co[p]}{4}"].value = Octant.count(1)
				elif(co[p]=="P"):
					ws[f"{co[p]}{4}"].value = Octant.count(-1)
				elif(co[p]=="Q"):
					ws[f"{co[p]}{4}"].value = Octant.count(2)
				elif(co[p]=="R"):
					ws[f"{co[p]}{4}"].value = Octant.count(-2)
				elif(co[p]=="S"):
					ws[f"{co[p]}{4}"].value = Octant.count(3)
				elif(co[p]=="T"):
					ws[f"{co[p]}{4}"].value = Octant.count(-3)
				elif(co[p]=="U"):
					ws[f"{co[p]}{4}"].value = Octant.count(4)
				elif(co[p]=="V"):
					ws[f"{co[p]}{4}"].value = Octant.count(-4)
				elif(co[p]=="W"):
					ws[f"{co[p]}{4}"].value = r1
					if(r1==1):
						ws[f"{co[p]}{4}"].fill = PatternFill("solid", fgColor="00FFFF00")
				elif(co[p]=="X"):
					ws[f"{co[p]}{4}"].value = r2
					if(r2==1):
						ws[f"{co[p]}{4}"].fill = PatternFill("solid", fgColor="00FFFF00")
				elif(co[p]=="Y"):
					ws[f"{co[p]}{4}"].value = r3
					if(r3==1):
						ws[f"{co[p]}{4}"].fill = PatternFill("solid", fgColor="00FFFF00")
				elif(co[p]=="Z"):
					ws[f"{co[p]}{4}"].value = r4
					if(r4==1):
						ws[f"{co[p]}{4}"].fill = PatternFill("solid", fgColor="00FFFF00")
				elif(co[p]=="AA"):
					ws[f"{co[p]}{4}"].value = r5
					if(r5==1):
						ws[f"{co[p]}{4}"].fill = PatternFill("solid", fgColor="00FFFF00")
				elif(co[p]=="AB"):
					ws[f"{co[p]}{4}"].value = r6
					if(r6==1):
						ws[f"{co[p]}{4}"].fill = PatternFill("solid", fgColor="00FFFF00")
				elif(co[p]=="AC"):
					ws[f"{co[p]}{4}"].value = r7
					if(r7==1):
						ws[f"{co[p]}{4}"].fill = PatternFill("solid", fgColor="00FFFF00")
				elif(co[p]=="AD"):
					ws[f"{co[p]}{4}"].value = r8
					if(r8==1):
						ws[f"{co[p]}{4}"].fill = PatternFill("solid", fgColor="00FFFF00")
				elif(co[p]=="AE"):
					ws[f"{co[p]}{4}"].value = ro
				elif(co[p]=="AF"):
					ws[f"{co[p]}{4}"].value = rn

			b=4
			ofc = []
			for k in range(0, len(d["T"]), mod):
				b+=1
				for p in range(len(co)):

					ws[f"{co[p]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
					OctantName = ["Internal outward interaction", "External outward interaction", "External Ejection", "Internal Ejection", "External inward interaction", "Internal inward interaction", "Internal sweep", "External sweep"]
					rr = [Octant[k:k+mod].count(1), Octant[k:k+mod].count(-1), Octant[k:k+mod].count(2), Octant[k:k+mod].count(-2), Octant[k:k+mod].count(3), Octant[k:k+mod].count(-3), Octant[k:k+mod].count(4), Octant[k:k+mod].count(-4)]
					rrr = [Octant[k:k+mod].count(1), Octant[k:k+mod].count(-1), Octant[k:k+mod].count(2), Octant[k:k+mod].count(-2), Octant[k:k+mod].count(3), Octant[k:k+mod].count(-3), Octant[k:k+mod].count(4), Octant[k:k+mod].count(-4)]
					rrr.sort(reverse=True)
					r1=r2=r3=r4=r5=r6=r7=r8=c=0
					for i in range(8):
						c=0
						for j in range(8):
							if(rr[i]==rrr[j]):
								if(j==0):
									if(i==0):
										ro=1
									elif(i==1):
										ro=-1
									elif(i==2):
										ro=2
									elif(i==3):
										ro=-2
									elif(i==4):
										ro=3
									elif(i==5):
										ro=-3
									elif(i==6):
										ro=4
									elif(i==7):
										ro=-4
									rn=OctantName[i]
									
								if(i==0):
									r1=(j+1)
								elif(i==1):
									r2=(j+1)
								elif(i==2):
									r3=(j+1)
								elif(i==3):
									r4=(j+1)
								elif(i==4):
									r5=(j+1)
								elif(i==5):
									r6=(j+1)
								elif(i==6):
									r7=(j+1)
								elif(i==7):
									r8=(j+1)
								c=1
							if(c==1):
								break
					if(co[p]=="N"):
						ws[f"{co[p]}{b}"].value = str(k) + "-" + str(k+mod-1)
					elif(co[p]=="O"):
						ws[f"{co[p]}{b}"].value = Octant[k:k+mod].count(1)
					elif(co[p]=="P"):
						ws[f"{co[p]}{b}"].value = Octant[k:k+mod].count(-1)
					elif(co[p]=="Q"):
						ws[f"{co[p]}{b}"].value = Octant[k:k+mod].count(2)
					elif(co[p]=="R"):
						ws[f"{co[p]}{b}"].value = Octant[k:k+mod].count(-2)
					elif(co[p]=="S"):
						ws[f"{co[p]}{b}"].value = Octant[k:k+mod].count(3)
					elif(co[p]=="T"):
						ws[f"{co[p]}{b}"].value = Octant[k:k+mod].count(-3)
					elif(co[p]=="U"):
						ws[f"{co[p]}{b}"].value = Octant[k:k+mod].count(4)
					elif(co[p]=="V"):
						ws[f"{co[p]}{b}"].value = Octant[k:k+mod].count(-4)
					elif(co[p]=="W"):
						ws[f"{co[p]}{b}"].value = r1
						if(r1==1):
							ws[f"{co[p]}{b}"].fill = PatternFill("solid", fgColor="00FFFF00")
					elif(co[p]=="X"):
						ws[f"{co[p]}{b}"].value = r2
						if(r2==1):
							ws[f"{co[p]}{b}"].fill = PatternFill("solid", fgColor="00FFFF00")
					elif(co[p]=="Y"):
						ws[f"{co[p]}{b}"].value = r3
						if(r3==1):
							ws[f"{co[p]}{b}"].fill = PatternFill("solid", fgColor="00FFFF00")
					elif(co[p]=="Z"):
						ws[f"{co[p]}{b}"].value = r4
						if(r4==1):
							ws[f"{co[p]}{b}"].fill = PatternFill("solid", fgColor="00FFFF00")
					elif(co[p]=="AA"):
						ws[f"{co[p]}{b}"].value = r5
						if(r5==1):
							ws[f"{co[p]}{b}"].fill = PatternFill("solid", fgColor="00FFFF00")
					elif(co[p]=="AB"):
						ws[f"{co[p]}{b}"].value = r6
						if(r6==1):
							ws[f"{co[p]}{b}"].fill = PatternFill("solid", fgColor="00FFFF00")
					elif(co[p]=="AC"):
						ws[f"{co[p]}{b}"].value = r7
						if(r7==1):
							ws[f"{co[p]}{b}"].fill = PatternFill("solid", fgColor="00FFFF00")
					elif(co[p]=="AD"):
						ws[f"{co[p]}{b}"].value = r8
						if(r8==1):
							ws[f"{co[p]}{b}"].fill = PatternFill("solid", fgColor="00FFFF00")
					elif(co[p]=="AE"):
						ws[f"{co[p]}{b}"].value = ro
					elif(co[p]=="AF"):
						ws[f"{co[p]}{b}"].value = rn
						ofc.append(rn)

			b+=2
			g = ["AC", "AD", "AE"]
			ws[f"{g[0]}{b}"].value = "Octant ID"
			ws[f"{g[1]}{b}"].value = "Octant Name"
			ws[f"{g[2]}{b}"].value = "Count of Rank 1 Mod Values"
			ws[f"{g[0]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
			ws[f"{g[1]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
			ws[f"{g[2]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
			b+=1

			oo = [1, -1, 2, -2, 3, -3, 4, -4]
			for i in range(8):
				ws[f"{g[0]}{b+i}"].value = oo[i]
				ws[f"{g[1]}{b+i}"].value = OctantName[i]
				ws[f"{g[2]}{b+i}"].value = ofc.count(OctantName[i])
				ws[f"{g[0]}{b+i}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
				ws[f"{g[1]}{b+i}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
				ws[f"{g[2]}{b+i}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)


			cc = "AH"
			ws[f"{cc}{4}"].value = "From"
			b = 18
			for i in range(0, len(d["T"]), mod):
				ws[f"{cc}{b}"].value = "From"
				b+=13
			
			transition_1 = []
			transition_11 = []
			transition_2 = []
			transition_22 = []
			transition_3 = []
			transition_33 = []
			transition_4 = []
			transition_44 = []
			
			for i in range(0, (len(d["T"]))-1, 1):
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

			cc = "AI"
			ws[f"{cc}{1}"].value = "Overall Transition Count"
			cc = "AJ"
			ws[f"{cc}{2}"].value = "To"

			gg = ["AI", "AJ", "AK", "AL", "AM", "AN", "AO", "AP", "AQ"]

			for i in range(len(gg)):
				if(i==0):
					ws[f"{gg[i]}{3}"].value = "Octant #"
				else:
					ws[f"{gg[i]}{3}"].value = oo[i-1]
				ws[f"{gg[i]}{3}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)

			b=4
			for i in range(8):
				ma = -1
				rc = 0
				cr =0
				for j in range(len(gg)):
					if(j==0):
						ws[f"{gg[j]}{b+i}"].value = oo[i]
					elif(j==1):
						ws[f"{gg[j]}{b+i}"].value = transition_1.count(oo[i])
						if(ma<transition_1.count(oo[i])):
							ma = transition_1.count(oo[i])
							rc = b+i
							cr = gg[j]
					elif(j==2):
						ws[f"{gg[j]}{b+i}"].value = transition_11.count(oo[i])
						if(ma<transition_11.count(oo[i])):
							ma = transition_11.count(oo[i])
							rc = b+i
							cr = gg[j]
					elif(j==3):
						ws[f"{gg[j]}{b+i}"].value = transition_2.count(oo[i])
						if(ma<transition_2.count(oo[i])):
							ma = transition_2.count(oo[i])
							rc = b+i
							cr = gg[j]
					elif(j==4):
						ws[f"{gg[j]}{b+i}"].value = transition_22.count(oo[i])
						if(ma<transition_22.count(oo[i])):
							ma = transition_22.count(oo[i])
							rc = b+i
							cr = gg[j]
					elif(j==5):
						ws[f"{gg[j]}{b+i}"].value = transition_3.count(oo[i])
						if(ma<transition_3.count(oo[i])):
							ma = transition_3.count(oo[i])
							rc = b+i
							cr = gg[j]
					elif(j==6):
						ws[f"{gg[j]}{b+i}"].value = transition_33.count(oo[i])
						if(ma<transition_33.count(oo[i])):
							ma = transition_33.count(oo[i])
							rc = b+i
							cr = gg[j]
					elif(j==7):
						ws[f"{gg[j]}{b+i}"].value = transition_4.count(oo[i])
						if(ma<transition_4.count(oo[i])):
							ma = transition_4.count(oo[i])
							rc = b+i
							cr = gg[j]
					elif(j==8):
						ws[f"{gg[j]}{b+i}"].value = transition_44.count(oo[i])
						if(ma<transition_44.count(oo[i])):
							ma = transition_44.count(oo[i])
							rc = b+i
							cr = gg[j]
					ws[f"{gg[j]}{b+i}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
				ws[f"{cr}{rc}"].fill = PatternFill("solid", fgColor="00FFFF00")
			b=15
			for ti in range(0, len(d["T"]), mod):
				ws[f"{gg[0]}{b}"].value = "Mod Transition Count"
				b+=1
				ws[f"{gg[0]}{b}"].value = str(ti)+"-"+str(ti+mod-1)
				ws[f"{gg[1]}{b}"].value = "To"
				b+=1
				for j in range(len(gg)):
					if(j==0):
						ws[f"{gg[j]}{b}"].value = "Octant #"
					else:
						ws[f"{gg[j]}{b}"].value = oo[j-1]
					ws[f"{gg[j]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
				transition_01 = []
				transition_011 = []
				transition_02 = []
				transition_022 = []
				transition_03 = []
				transition_033 = []
				transition_04 = []
				transition_044 = []
			
				for i in range(ti, ti+mod, 1):
					if(i<len(d["T"])-1):
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

				b+=1
				for i in range(8):
					ma = -1
					rc = 0
					cr =0
					for j in range(len(gg)):
						if(j==0):
							ws[f"{gg[j]}{b+i}"].value = oo[i]
						elif(j==1):
							ws[f"{gg[j]}{b+i}"].value = transition_1.count(oo[i])
							if(ma<transition_1.count(oo[i])):
								ma = transition_1.count(oo[i])
								rc = b+i
								cr = gg[j]
						elif(j==2):
							ws[f"{gg[j]}{b+i}"].value = transition_11.count(oo[i])
							if(ma<transition_11.count(oo[i])):
								ma = transition_11.count(oo[i])
								rc = b+i
								cr = gg[j]
						elif(j==3):
							ws[f"{gg[j]}{b+i}"].value = transition_2.count(oo[i])
							if(ma<transition_2.count(oo[i])):
								ma = transition_2.count(oo[i])
								rc = b+i
								cr = gg[j]
						elif(j==4):
							ws[f"{gg[j]}{b+i}"].value = transition_22.count(oo[i])
							if(ma<transition_22.count(oo[i])):
								ma = transition_22.count(oo[i])
								rc = b+i
								cr = gg[j]
						elif(j==5):
							ws[f"{gg[j]}{b+i}"].value = transition_3.count(oo[i])
							if(ma<transition_3.count(oo[i])):
								ma = transition_3.count(oo[i])
								rc = b+i
								cr = gg[j]
						elif(j==6):
							ws[f"{gg[j]}{b+i}"].value = transition_33.count(oo[i])
							if(ma<transition_33.count(oo[i])):
								ma = transition_33.count(oo[i])
								rc = b+i
								cr = gg[j]
						elif(j==7):
							ws[f"{gg[j]}{b+i}"].value = transition_4.count(oo[i])
							if(ma<transition_4.count(oo[i])):
								ma = transition_4.count(oo[i])
								rc = b+i
								cr = gg[j]
						elif(j==8):
							ws[f"{gg[j]}{b+i}"].value = transition_44.count(oo[i])
							if(ma<transition_44.count(oo[i])):
								ma = transition_44.count(oo[i])
								rc = b+i
								cr = gg[j]
						ws[f"{gg[j]}{b+i}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
					ws[f"{cr}{rc}"].fill = PatternFill("solid", fgColor="00FFFF00")
				b+=10

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
			for i in range(len(d["T"])):
				if(i==0):
					v=1
				elif(Octant[i]==Octant[i-1]):
					v+=1
				else:
					if(Octant[i-1]==1 and u1<=v):
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
					elif(Octant[i-1]==2 and u3<=v):
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
					elif(Octant[i-1]==3 and u5<=v):
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
					elif(Octant[i-1]==4 and u7<=v):
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
			if(Octant[len(d["T"])-1]==1 and u1<=v):
				if(u1<v):
					u11=1
				else:
					u11+=1
				u1=v
			elif(Octant[len(d["T"])-1]==-1 and u2<=v):
				if(u2<v):
					u22=1
				else:
					u22+=1
				u2=v
			elif(Octant[len(d["T"])-1]==2 and u3<=v):
				if(u3<v):
					u33=1
				else:
					u33+=1
				u3=v
			elif(Octant[len(d["T"])-1]==-2 and u4<=v):
				if(u4<v):
					u44=1
				else:
					u44+=1
				u4=v
			elif(Octant[len(d["T"])-1]==3 and u5<=v):
				if(u5<v):
					u55=1
				else:
					u55+=1
				u5=v
			elif(Octant[len(d["T"])-1]==-3 and u6<=v):
				if(u6<v):
					u66=1
				else:
					u66+=1
				u6=v
			elif(Octant[len(d["T"])-1]==4 and u7<=v):
				if(u7<v):
					u77=1
				else:
					u77+=1
				u7=v
			elif(Octant[len(d["T"])-1]==-4 and u8<=v):
				if(u8<v):
					u88=1
				else:
					u88+=1
				u8=v
			e=0
			for i in range(len(d["T"])):
				if(i==0):
					e=1
				elif(Octant[i]==Octant[i-1]):
					e+=1
				elif(Octant[i]!=Octant[i-1]):
					if(Octant[i-1]==1 and e==u1):
						f1.append(d["T"][i-e])
						t1.append(d["T"][i-1])
					elif(Octant[i-1]==-1 and e==u2):
						f2.append(d["T"][i-e])
						t2.append(d["T"][i-1])
					elif(Octant[i-1]==2 and e==u3):
						f3.append(d["T"][i-e])
						t3.append(d["T"][i-1])
					elif(Octant[i-1]==-2 and e==u4):
						f4.append(d["T"][i-e])
						t4.append(d["T"][i-1])
					elif(Octant[i-1]==3 and e==u5):
						f5.append(d["T"][i-e])
						t5.append(d["T"][i-1])
					elif(Octant[i-1]==-3 and e==u6):
						f6.append(d["T"][i-e])
						t6.append(d["T"][i-1])
					elif(Octant[i-1]==4 and e==u7):
						f7.append(d["T"][i-e])
						t7.append(d["T"][i-1])
					elif(Octant[i-1]==-4 and e==u8):
						f8.append(d["T"][i-e])
						t8.append(d["T"][i-1])
					e=1
			if(Octant[len(d["T"])-1]==1 and e==u1):
				f1.append(d["T"][len(d["T"])-e])
				t1.append(d["T"][len(d["T"])-1])
			elif(Octant[len(d["T"])-1]==-1 and e==u2):
				f2.append(d["T"][len(d["T"])-e])
				t2.append(d["T"][len(d["T"])-1])
			elif(Octant[len(d["T"])-1]==2 and e==u3):
				f3.append(d["T"][len(d["T"])-e])
				t3.append(d["T"][len(d["T"])-1])
			elif(Octant[len(d["T"])-1]==-2 and e==u4):
				f4.append(d["T"][len(d["T"])-e])
				t4.append(d["T"][len(d["T"])-1])
			elif(Octant[len(d["T"])-1]==3 and e==u5):
				f5.append(d["T"][len(d["T"])-e])
				t5.append(d["T"][len(d["T"])-1])
			elif(Octant[len(d["T"])-1]==-3 and e==u6):
				f6.append(d["T"][len(d["T"])-e])
				t6.append(d["T"][len(d["T"])-1])
			elif(Octant[len(d["T"])-1]==4 and e==u7):
				f7.append(d["T"][len(d["T"])-e])
				t7.append(d["T"][len(d["T"])-1])
			elif(Octant[len(d["T"])-1]==-4 and e==u8):
				f8.append(d["T"][len(d["T"])-e])
				t8.append(d["T"][len(d["T"])-1])
			longest_subsequence = [u1,u2,u3,u4,u5,u6,u7,u8]
			cnt = [u11,u22,u33,u44,u55,u66,u77,u88]

			ccc = ["AS", "AT", "AU"]
			ws[f"{ccc[0]}{1}"].value = "Longest Subsequence Length"
			ws[f"{ccc[0]}{3}"].value = "Octant ##"
			ws[f"{ccc[1]}{3}"].value = "Longest Subsequence Length"
			ws[f"{ccc[2]}{3}"].value = "Count"
			ws[f"{ccc[0]}{3}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
			ws[f"{ccc[1]}{3}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
			ws[f"{ccc[2]}{3}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)

			b=4
			for i in range(8):
				ws[f"{ccc[0]}{b}"].value = oo[i]
				ws[f"{ccc[1]}{b}"].value = longest_subsequence[i]
				ws[f"{ccc[2]}{b}"].value = cnt[i]
				ws[f"{ccc[0]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
				ws[f"{ccc[1]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
				ws[f"{ccc[2]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)

				b+=1
			
			df = ["AW", "AX", "AY"]
			ws[f"{df[0]}{1}"].value = "Longest Subsequence Length with Range"
			ws[f"{df[0]}{3}"].value = "Octant ###"
			ws[f"{df[1]}{3}"].value = "Longest Subsequence Length"
			ws[f"{df[2]}{3}"].value = "Count"
			ws[f"{df[0]}{3}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
			ws[f"{df[1]}{3}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
			ws[f"{df[2]}{3}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)

			b=4

			for i in range(8):
				ws[f"{df[0]}{b}"].value = oo[i]
				ws[f"{df[1]}{b}"].value = longest_subsequence[i]
				ws[f"{df[2]}{b}"].value = cnt[i]
				ws[f"{df[0]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
				ws[f"{df[1]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
				ws[f"{df[2]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)

				b+=1
				ws[f"{df[0]}{b}"].value = "Time"
				ws[f"{df[1]}{b}"].value = "From"
				ws[f"{df[2]}{b}"].value = "To"
				ws[f"{df[0]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
				ws[f"{df[1]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
				ws[f"{df[2]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)

				b+=1
				for j in range(cnt[i]):
					if(i==0):
						ws[f"{df[1]}{b}"].value = f1[j]
						ws[f"{df[2]}{b}"].value = t1[j]
						ws[f"{df[0]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
						ws[f"{df[1]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
						ws[f"{df[2]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)

						b+=1

					elif(i==1):
						ws[f"{df[1]}{b}"].value = f2[j]
						ws[f"{df[2]}{b}"].value = t2[j]
						ws[f"{df[0]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
						ws[f"{df[1]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
						ws[f"{df[2]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)

						b+=1

					elif(i==2):
						ws[f"{df[1]}{b}"].value = f3[j]
						ws[f"{df[2]}{b}"].value = t3[j]
						ws[f"{df[0]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
						ws[f"{df[1]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
						ws[f"{df[2]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
						
						b+=1

					elif(i==3):
						ws[f"{df[1]}{b}"].value = f4[j]
						ws[f"{df[2]}{b}"].value = t4[j]
						ws[f"{df[0]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
						ws[f"{df[1]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
						ws[f"{df[2]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
						
						b+=1

					elif(i==4):
						ws[f"{df[1]}{b}"].value = f5[j]
						ws[f"{df[2]}{b}"].value = t5[j]
						ws[f"{df[0]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
						ws[f"{df[1]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
						ws[f"{df[2]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
						
						b+=1

					elif(i==5):
						ws[f"{df[1]}{b}"].value = f6[j]
						ws[f"{df[2]}{b}"].value = t6[j]
						ws[f"{df[0]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
						ws[f"{df[1]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
						ws[f"{df[2]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
						
						b+=1

					elif(i==6):
						ws[f"{df[1]}{b}"].value = f7[j]
						ws[f"{df[2]}{b}"].value = t7[j]
						ws[f"{df[0]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
						ws[f"{df[1]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
						ws[f"{df[2]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
						
						b+=1

					elif(i==7):
						ws[f"{df[1]}{b}"].value = f8[j]
						ws[f"{df[2]}{b}"].value = t8[j]
						ws[f"{df[0]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
						ws[f"{df[1]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
						ws[f"{df[2]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
						
						b+=1
			fd = file.split('\\')[-1].split('.xlsx')[0]
			print(fd)
			strout = 'output\\'+str(fd)+"_"+str(mod)+"_"+str(datetime.now().year)+"-"+str(datetime.now().month)+"-"+str(datetime.now().day)+"-"+str(datetime.now().hour)+"-"+str(datetime.now().minute)+"-"+str(datetime.now().second)+".xlsx"
			print(strout)
			try:
				os.makedirs("output\\")
				wb.save(filename= strout)
			except OSError as e:
				wb.save(filename= strout)


	except:
		import streamlit as st
		st.write("Check the path to required folder.")
		

def octant_analysis_single(file, mod=5000):
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
		#import xlsxwriter
		from io import BytesIO
		#output = BytesIO()

		wb = Workbook()
		#with NamedTemporaryFile() as tmp:
		#	wb.save(tmp.name)
		#	data = BytesIO(tmp.read())
		ws = wb.active
		#ws.title = "output"
		#wb = xlsxwriter.Workbook(output, engine='xlsxwriter')
		#ws = workbook.add_worksheet()




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
			

		for i in range(len(col)):
			ws[f"{col[i]}{ri}"].value = text[i]
			for r in range(3,len(d_1)+3):
				ws[f"{col[i]}{r}"].value = wh[i][r-3]
		c= "M"
		ws[f"{c}{4}"].value = "Mod " + str(mod)

		c= "N"
		ws[f"{c}{1}"].value = "Overall Octant Count"

		thin = Side(border_style="thin", color="000000")

		co = ["N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "AA", "AB", "AC", "AD", "AE", "AF"]
		tex = ["Octant ID", "+1", "-1", "+2", "-2", "+3", "-3", "+4", "-4", "Rank Octant 1", "Rank Octant -1", "Rank Octant 2", "Rank Octant -2", "Rank Octant 3", "Rank Octant -3", "Rank Octant 4", "Rank Octant -4", "Rank1 Octant ID", "Rank1 Octant Name"]

		for i in range(len(co)):
			ws[f"{co[i]}{3}"].value = tex[i]
			ws[f"{co[i]}{3}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)

		for p in range(len(co)):

			ws[f"{co[p]}{4}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
			OctantName = ["Internal outward interaction", "External outward interaction", "External Ejection", "Internal Ejection", "External inward interaction", "Internal inward interaction", "Internal sweep", "External sweep"]
			rr = [Octant.count(1), Octant.count(-1), Octant.count(2), Octant.count(-2), Octant.count(3), Octant.count(-3), Octant.count(4), Octant.count(-4)]
			rrr = [Octant.count(1), Octant.count(-1), Octant.count(2), Octant.count(-2), Octant.count(3), Octant.count(-3), Octant.count(4), Octant.count(-4)]
			rrr.sort(reverse=True)
			r1=r2=r3=r4=r5=r6=r7=r8=c=0
			for i in range(8):
				c=0
				for j in range(8):
					if(rr[i]==rrr[j]):
						if(j==0):
							if(i==0):
								ro=1
							elif(i==1):
								ro=-1
							elif(i==2):
								ro=2
							elif(i==3):
								ro=-2
							elif(i==4):
								ro=3
							elif(i==5):
								ro=-3
							elif(i==6):
								ro=4
							elif(i==7):
								ro=-4
							rn=OctantName[i]
						if(i==0):
							r1=(j+1)
						elif(i==1):
							r2=(j+1)
						elif(i==2):
							r3=(j+1)
						elif(i==3):
							r4=(j+1)
						elif(i==4):
							r5=(j+1)
						elif(i==5):
							r6=(j+1)
						elif(i==6):
							r7=(j+1)
						elif(i==7):
							r8=(j+1)
						c=1
					if(c==1):
						break
			if(co[p]=="N"):
				ws[f"{co[p]}{4}"].value = "Overall Count"
			elif(co[p]=="O"):
				ws[f"{co[p]}{4}"].value = Octant.count(1)
			elif(co[p]=="P"):
				ws[f"{co[p]}{4}"].value = Octant.count(-1)
			elif(co[p]=="Q"):
				ws[f"{co[p]}{4}"].value = Octant.count(2)
			elif(co[p]=="R"):
				ws[f"{co[p]}{4}"].value = Octant.count(-2)
			elif(co[p]=="S"):
				ws[f"{co[p]}{4}"].value = Octant.count(3)
			elif(co[p]=="T"):
				ws[f"{co[p]}{4}"].value = Octant.count(-3)
			elif(co[p]=="U"):
				ws[f"{co[p]}{4}"].value = Octant.count(4)
			elif(co[p]=="V"):
				ws[f"{co[p]}{4}"].value = Octant.count(-4)
			elif(co[p]=="W"):
				ws[f"{co[p]}{4}"].value = r1
				if(r1==1):
					ws[f"{co[p]}{4}"].fill = PatternFill("solid", fgColor="00FFFF00")
			elif(co[p]=="X"):
				ws[f"{co[p]}{4}"].value = r2
				if(r2==1):
					ws[f"{co[p]}{4}"].fill = PatternFill("solid", fgColor="00FFFF00")
			elif(co[p]=="Y"):
				ws[f"{co[p]}{4}"].value = r3
				if(r3==1):
					ws[f"{co[p]}{4}"].fill = PatternFill("solid", fgColor="00FFFF00")
			elif(co[p]=="Z"):
				ws[f"{co[p]}{4}"].value = r4
				if(r4==1):
					ws[f"{co[p]}{4}"].fill = PatternFill("solid", fgColor="00FFFF00")
			elif(co[p]=="AA"):
				ws[f"{co[p]}{4}"].value = r5
				if(r5==1):
					ws[f"{co[p]}{4}"].fill = PatternFill("solid", fgColor="00FFFF00")
			elif(co[p]=="AB"):
				ws[f"{co[p]}{4}"].value = r6
				if(r6==1):
					ws[f"{co[p]}{4}"].fill = PatternFill("solid", fgColor="00FFFF00")
			elif(co[p]=="AC"):
				ws[f"{co[p]}{4}"].value = r7
				if(r7==1):
					ws[f"{co[p]}{4}"].fill = PatternFill("solid", fgColor="00FFFF00")
			elif(co[p]=="AD"):
				ws[f"{co[p]}{4}"].value = r8
				if(r8==1):
					ws[f"{co[p]}{4}"].fill = PatternFill("solid", fgColor="00FFFF00")
			elif(co[p]=="AE"):
				ws[f"{co[p]}{4}"].value = ro
			elif(co[p]=="AF"):
				ws[f"{co[p]}{4}"].value = rn

		b=4
		ofc = []
		for k in range(0, len(d["T"]), mod):
			b+=1
			for p in range(len(co)):

				ws[f"{co[p]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
				OctantName = ["Internal outward interaction", "External outward interaction", "External Ejection", "Internal Ejection", "External inward interaction", "Internal inward interaction", "Internal sweep", "External sweep"]
				rr = [Octant[k:k+mod].count(1), Octant[k:k+mod].count(-1), Octant[k:k+mod].count(2), Octant[k:k+mod].count(-2), Octant[k:k+mod].count(3), Octant[k:k+mod].count(-3), Octant[k:k+mod].count(4), Octant[k:k+mod].count(-4)]
				rrr = [Octant[k:k+mod].count(1), Octant[k:k+mod].count(-1), Octant[k:k+mod].count(2), Octant[k:k+mod].count(-2), Octant[k:k+mod].count(3), Octant[k:k+mod].count(-3), Octant[k:k+mod].count(4), Octant[k:k+mod].count(-4)]
				rrr.sort(reverse=True)
				r1=r2=r3=r4=r5=r6=r7=r8=c=0
				for i in range(8):
					c=0
					for j in range(8):
						if(rr[i]==rrr[j]):
							if(j==0):
								if(i==0):
									ro=1
								elif(i==1):
									ro=-1
								elif(i==2):
									ro=2
								elif(i==3):
									ro=-2
								elif(i==4):
									ro=3
								elif(i==5):
									ro=-3
								elif(i==6):
									ro=4
								elif(i==7):
									ro=-4
								rn=OctantName[i]
									
							if(i==0):
								r1=(j+1)
							elif(i==1):
								r2=(j+1)
							elif(i==2):
								r3=(j+1)
							elif(i==3):
								r4=(j+1)
							elif(i==4):
								r5=(j+1)
							elif(i==5):
								r6=(j+1)
							elif(i==6):
								r7=(j+1)
							elif(i==7):
								r8=(j+1)
							c=1
						if(c==1):
							break
				if(co[p]=="N"):
					ws[f"{co[p]}{b}"].value = str(k) + "-" + str(k+mod-1)
				elif(co[p]=="O"):
					ws[f"{co[p]}{b}"].value = Octant[k:k+mod].count(1)
				elif(co[p]=="P"):
					ws[f"{co[p]}{b}"].value = Octant[k:k+mod].count(-1)
				elif(co[p]=="Q"):
					ws[f"{co[p]}{b}"].value = Octant[k:k+mod].count(2)
				elif(co[p]=="R"):
					ws[f"{co[p]}{b}"].value = Octant[k:k+mod].count(-2)
				elif(co[p]=="S"):
					ws[f"{co[p]}{b}"].value = Octant[k:k+mod].count(3)
				elif(co[p]=="T"):
					ws[f"{co[p]}{b}"].value = Octant[k:k+mod].count(-3)
				elif(co[p]=="U"):
					ws[f"{co[p]}{b}"].value = Octant[k:k+mod].count(4)
				elif(co[p]=="V"):
					ws[f"{co[p]}{b}"].value = Octant[k:k+mod].count(-4)
				elif(co[p]=="W"):
					ws[f"{co[p]}{b}"].value = r1
					if(r1==1):
						ws[f"{co[p]}{b}"].fill = PatternFill("solid", fgColor="00FFFF00")
				elif(co[p]=="X"):
					ws[f"{co[p]}{b}"].value = r2
					if(r2==1):
						ws[f"{co[p]}{b}"].fill = PatternFill("solid", fgColor="00FFFF00")
				elif(co[p]=="Y"):
					ws[f"{co[p]}{b}"].value = r3
					if(r3==1):
						ws[f"{co[p]}{b}"].fill = PatternFill("solid", fgColor="00FFFF00")
				elif(co[p]=="Z"):
					ws[f"{co[p]}{b}"].value = r4
					if(r4==1):
						ws[f"{co[p]}{b}"].fill = PatternFill("solid", fgColor="00FFFF00")
				elif(co[p]=="AA"):
					ws[f"{co[p]}{b}"].value = r5
					if(r5==1):
						ws[f"{co[p]}{b}"].fill = PatternFill("solid", fgColor="00FFFF00")
				elif(co[p]=="AB"):
					ws[f"{co[p]}{b}"].value = r6
					if(r6==1):
						ws[f"{co[p]}{b}"].fill = PatternFill("solid", fgColor="00FFFF00")
				elif(co[p]=="AC"):
					ws[f"{co[p]}{b}"].value = r7
					if(r7==1):
						ws[f"{co[p]}{b}"].fill = PatternFill("solid", fgColor="00FFFF00")
				elif(co[p]=="AD"):
					ws[f"{co[p]}{b}"].value = r8
					if(r8==1):
						ws[f"{co[p]}{b}"].fill = PatternFill("solid", fgColor="00FFFF00")
				elif(co[p]=="AE"):
					ws[f"{co[p]}{b}"].value = ro
				elif(co[p]=="AF"):
					ws[f"{co[p]}{b}"].value = rn
					ofc.append(rn)

		b+=2
		g = ["AC", "AD", "AE"]
		ws[f"{g[0]}{b}"].value = "Octant ID"
		ws[f"{g[1]}{b}"].value = "Octant Name"
		ws[f"{g[2]}{b}"].value = "Count of Rank 1 Mod Values"
		ws[f"{g[0]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
		ws[f"{g[1]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
		ws[f"{g[2]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
		b+=1

		oo = [1, -1, 2, -2, 3, -3, 4, -4]
		for i in range(8):
			ws[f"{g[0]}{b+i}"].value = oo[i]
			ws[f"{g[1]}{b+i}"].value = OctantName[i]
			ws[f"{g[2]}{b+i}"].value = ofc.count(OctantName[i])
			ws[f"{g[0]}{b+i}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
			ws[f"{g[1]}{b+i}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
			ws[f"{g[2]}{b+i}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)


		cc = "AH"
		ws[f"{cc}{4}"].value = "From"
		b = 18
		for i in range(0, len(d["T"]), mod):
			ws[f"{cc}{b}"].value = "From"
			b+=13
			
		transition_1 = []
		transition_11 = []
		transition_2 = []
		transition_22 = []
		transition_3 = []
		transition_33 = []
		transition_4 = []
		transition_44 = []
			
		for i in range(0, (len(d["T"]))-1, 1):
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

		cc = "AI"
		ws[f"{cc}{1}"].value = "Overall Transition Count"
		cc = "AJ"
		ws[f"{cc}{2}"].value = "To"

		gg = ["AI", "AJ", "AK", "AL", "AM", "AN", "AO", "AP", "AQ"]

		for i in range(len(gg)):
			if(i==0):
				ws[f"{gg[i]}{3}"].value = "Octant #"
			else:
				ws[f"{gg[i]}{3}"].value = oo[i-1]
			ws[f"{gg[i]}{3}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)

		b=4
		for i in range(8):
			ma = -1
			rc = 0
			cr =0
			for j in range(len(gg)):
				if(j==0):
					ws[f"{gg[j]}{b+i}"].value = oo[i]
				elif(j==1):
					ws[f"{gg[j]}{b+i}"].value = transition_1.count(oo[i])
					if(ma<transition_1.count(oo[i])):
						ma = transition_1.count(oo[i])
						rc = b+i
						cr = gg[j]
				elif(j==2):
					ws[f"{gg[j]}{b+i}"].value = transition_11.count(oo[i])
					if(ma<transition_11.count(oo[i])):
						ma = transition_11.count(oo[i])
						rc = b+i
						cr = gg[j]
				elif(j==3):
					ws[f"{gg[j]}{b+i}"].value = transition_2.count(oo[i])
					if(ma<transition_2.count(oo[i])):
						ma = transition_2.count(oo[i])
						rc = b+i
						cr = gg[j]
				elif(j==4):
					ws[f"{gg[j]}{b+i}"].value = transition_22.count(oo[i])
					if(ma<transition_22.count(oo[i])):
						ma = transition_22.count(oo[i])
						rc = b+i
						cr = gg[j]
				elif(j==5):
					ws[f"{gg[j]}{b+i}"].value = transition_3.count(oo[i])
					if(ma<transition_3.count(oo[i])):
						ma = transition_3.count(oo[i])
						rc = b+i
						cr = gg[j]
				elif(j==6):
					ws[f"{gg[j]}{b+i}"].value = transition_33.count(oo[i])
					if(ma<transition_33.count(oo[i])):
						ma = transition_33.count(oo[i])
						rc = b+i
						cr = gg[j]
				elif(j==7):
					ws[f"{gg[j]}{b+i}"].value = transition_4.count(oo[i])
					if(ma<transition_4.count(oo[i])):
						ma = transition_4.count(oo[i])
						rc = b+i
						cr = gg[j]
				elif(j==8):
					ws[f"{gg[j]}{b+i}"].value = transition_44.count(oo[i])
					if(ma<transition_44.count(oo[i])):
						ma = transition_44.count(oo[i])
						rc = b+i
						cr = gg[j]
				ws[f"{gg[j]}{b+i}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
			ws[f"{cr}{rc}"].fill = PatternFill("solid", fgColor="00FFFF00")
		b=15
		for ti in range(0, len(d["T"]), mod):
			ws[f"{gg[0]}{b}"].value = "Mod Transition Count"
			b+=1
			ws[f"{gg[0]}{b}"].value = str(ti)+"-"+str(ti+mod-1)
			ws[f"{gg[1]}{b}"].value = "To"
			b+=1
			for j in range(len(gg)):
				if(j==0):
					ws[f"{gg[j]}{b}"].value = "Octant #"
				else:
					ws[f"{gg[j]}{b}"].value = oo[j-1]
				ws[f"{gg[j]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
			transition_01 = []
			transition_011 = []
			transition_02 = []
			transition_022 = []
			transition_03 = []
			transition_033 = []
			transition_04 = []
			transition_044 = []
			
			for i in range(ti, ti+mod, 1):
				if(i<len(d["T"])-1):
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

			b+=1
			for i in range(8):
				ma = -1
				rc = 0
				cr =0
				for j in range(len(gg)):
					if(j==0):
						ws[f"{gg[j]}{b+i}"].value = oo[i]
					elif(j==1):
						ws[f"{gg[j]}{b+i}"].value = transition_1.count(oo[i])
						if(ma<transition_1.count(oo[i])):
							ma = transition_1.count(oo[i])
							rc = b+i
							cr = gg[j]
					elif(j==2):
						ws[f"{gg[j]}{b+i}"].value = transition_11.count(oo[i])
						if(ma<transition_11.count(oo[i])):
							ma = transition_11.count(oo[i])
							rc = b+i
							cr = gg[j]
					elif(j==3):
						ws[f"{gg[j]}{b+i}"].value = transition_2.count(oo[i])
						if(ma<transition_2.count(oo[i])):
							ma = transition_2.count(oo[i])
							rc = b+i
							cr = gg[j]
					elif(j==4):
						ws[f"{gg[j]}{b+i}"].value = transition_22.count(oo[i])
						if(ma<transition_22.count(oo[i])):
							ma = transition_22.count(oo[i])
							rc = b+i
							cr = gg[j]
					elif(j==5):
						ws[f"{gg[j]}{b+i}"].value = transition_3.count(oo[i])
						if(ma<transition_3.count(oo[i])):
							ma = transition_3.count(oo[i])
							rc = b+i
							cr = gg[j]
					elif(j==6):
						ws[f"{gg[j]}{b+i}"].value = transition_33.count(oo[i])
						if(ma<transition_33.count(oo[i])):
							ma = transition_33.count(oo[i])
							rc = b+i
							cr = gg[j]
					elif(j==7):
						ws[f"{gg[j]}{b+i}"].value = transition_4.count(oo[i])
						if(ma<transition_4.count(oo[i])):
							ma = transition_4.count(oo[i])
							rc = b+i
							cr = gg[j]
					elif(j==8):
						ws[f"{gg[j]}{b+i}"].value = transition_44.count(oo[i])
						if(ma<transition_44.count(oo[i])):
							ma = transition_44.count(oo[i])
							rc = b+i
							cr = gg[j]
					ws[f"{gg[j]}{b+i}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
				ws[f"{cr}{rc}"].fill = PatternFill("solid", fgColor="00FFFF00")
			b+=10

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
		for i in range(len(d["T"])):
			if(i==0):
				v=1
			elif(Octant[i]==Octant[i-1]):
				v+=1
			else:
				if(Octant[i-1]==1 and u1<=v):
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
				elif(Octant[i-1]==2 and u3<=v):
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
				elif(Octant[i-1]==3 and u5<=v):
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
				elif(Octant[i-1]==4 and u7<=v):
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
		if(Octant[len(d["T"])-1]==1 and u1<=v):
			if(u1<v):
				u11=1
			else:
				u11+=1
			u1=v
		elif(Octant[len(d["T"])-1]==-1 and u2<=v):
			if(u2<v):
				u22=1
			else:
				u22+=1
			u2=v
		elif(Octant[len(d["T"])-1]==2 and u3<=v):
			if(u3<v):
				u33=1
			else:
				u33+=1
			u3=v
		elif(Octant[len(d["T"])-1]==-2 and u4<=v):
			if(u4<v):
				u44=1
			else:
				u44+=1
			u4=v
		elif(Octant[len(d["T"])-1]==3 and u5<=v):
			if(u5<v):
				u55=1
			else:
				u55+=1
			u5=v
		elif(Octant[len(d["T"])-1]==-3 and u6<=v):
			if(u6<v):
				u66=1
			else:
				u66+=1
			u6=v
		elif(Octant[len(d["T"])-1]==4 and u7<=v):
			if(u7<v):
				u77=1
			else:
				u77+=1
			u7=v
		elif(Octant[len(d["T"])-1]==-4 and u8<=v):
			if(u8<v):
				u88=1
			else:
				u88+=1
			u8=v
		e=0
		for i in range(len(d["T"])):
			if(i==0):
				e=1
			elif(Octant[i]==Octant[i-1]):
				e+=1
			elif(Octant[i]!=Octant[i-1]):
				if(Octant[i-1]==1 and e==u1):
					f1.append(d["T"][i-e])
					t1.append(d["T"][i-1])
				elif(Octant[i-1]==-1 and e==u2):
					f2.append(d["T"][i-e])
					t2.append(d["T"][i-1])
				elif(Octant[i-1]==2 and e==u3):
					f3.append(d["T"][i-e])
					t3.append(d["T"][i-1])
				elif(Octant[i-1]==-2 and e==u4):
					f4.append(d["T"][i-e])
					t4.append(d["T"][i-1])
				elif(Octant[i-1]==3 and e==u5):
					f5.append(d["T"][i-e])
					t5.append(d["T"][i-1])
				elif(Octant[i-1]==-3 and e==u6):
					f6.append(d["T"][i-e])
					t6.append(d["T"][i-1])
				elif(Octant[i-1]==4 and e==u7):
					f7.append(d["T"][i-e])
					t7.append(d["T"][i-1])
				elif(Octant[i-1]==-4 and e==u8):
					f8.append(d["T"][i-e])
					t8.append(d["T"][i-1])
				e=1
		if(Octant[len(d["T"])-1]==1 and e==u1):
			f1.append(d["T"][len(d["T"])-e])
			t1.append(d["T"][len(d["T"])-1])
		elif(Octant[len(d["T"])-1]==-1 and e==u2):
			f2.append(d["T"][len(d["T"])-e])
			t2.append(d["T"][len(d["T"])-1])
		elif(Octant[len(d["T"])-1]==2 and e==u3):
			f3.append(d["T"][len(d["T"])-e])
			t3.append(d["T"][len(d["T"])-1])
		elif(Octant[len(d["T"])-1]==-2 and e==u4):
			f4.append(d["T"][len(d["T"])-e])
			t4.append(d["T"][len(d["T"])-1])
		elif(Octant[len(d["T"])-1]==3 and e==u5):
			f5.append(d["T"][len(d["T"])-e])
			t5.append(d["T"][len(d["T"])-1])
		elif(Octant[len(d["T"])-1]==-3 and e==u6):
			f6.append(d["T"][len(d["T"])-e])
			t6.append(d["T"][len(d["T"])-1])
		elif(Octant[len(d["T"])-1]==4 and e==u7):
			f7.append(d["T"][len(d["T"])-e])
			t7.append(d["T"][len(d["T"])-1])
		elif(Octant[len(d["T"])-1]==-4 and e==u8):
			f8.append(d["T"][len(d["T"])-e])
			t8.append(d["T"][len(d["T"])-1])
		longest_subsequence = [u1,u2,u3,u4,u5,u6,u7,u8]
		cnt = [u11,u22,u33,u44,u55,u66,u77,u88]

		ccc = ["AS", "AT", "AU"]
		ws[f"{ccc[0]}{1}"].value = "Longest Subsequence Length"
		ws[f"{ccc[0]}{3}"].value = "Octant ##"
		ws[f"{ccc[1]}{3}"].value = "Longest Subsequence Length"
		ws[f"{ccc[2]}{3}"].value = "Count"
		ws[f"{ccc[0]}{3}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
		ws[f"{ccc[1]}{3}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
		ws[f"{ccc[2]}{3}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)

		b=4
		for i in range(8):
			ws[f"{ccc[0]}{b}"].value = oo[i]
			ws[f"{ccc[1]}{b}"].value = longest_subsequence[i]
			ws[f"{ccc[2]}{b}"].value = cnt[i]
			ws[f"{ccc[0]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
			ws[f"{ccc[1]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
			ws[f"{ccc[2]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)

			b+=1
			
		df = ["AW", "AX", "AY"]
		ws[f"{df[0]}{1}"].value = "Longest Subsequence Length with Range"
		ws[f"{df[0]}{3}"].value = "Octant ###"
		ws[f"{df[1]}{3}"].value = "Longest Subsequence Length"
		ws[f"{df[2]}{3}"].value = "Count"
		ws[f"{df[0]}{3}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
		ws[f"{df[1]}{3}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
		ws[f"{df[2]}{3}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)

		b=4

		for i in range(8):
			ws[f"{df[0]}{b}"].value = oo[i]
			ws[f"{df[1]}{b}"].value = longest_subsequence[i]
			ws[f"{df[2]}{b}"].value = cnt[i]
			ws[f"{df[0]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
			ws[f"{df[1]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
			ws[f"{df[2]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)

			b+=1
			ws[f"{df[0]}{b}"].value = "Time"
			ws[f"{df[1]}{b}"].value = "From"
			ws[f"{df[2]}{b}"].value = "To"
			ws[f"{df[0]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
			ws[f"{df[1]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
			ws[f"{df[2]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)

			b+=1
			for j in range(cnt[i]):
				if(i==0):
					ws[f"{df[1]}{b}"].value = f1[j]
					ws[f"{df[2]}{b}"].value = t1[j]
					ws[f"{df[0]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
					ws[f"{df[1]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
					ws[f"{df[2]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)

					b+=1
				elif(i==1):
					ws[f"{df[1]}{b}"].value = f2[j]
					ws[f"{df[2]}{b}"].value = t2[j]
					ws[f"{df[0]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
					ws[f"{df[1]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
					ws[f"{df[2]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)

					b+=1

				elif(i==2):
					ws[f"{df[1]}{b}"].value = f3[j]
					ws[f"{df[2]}{b}"].value = t3[j]
					ws[f"{df[0]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
					ws[f"{df[1]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
					ws[f"{df[2]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
					
					b+=1

				elif(i==3):
					ws[f"{df[1]}{b}"].value = f4[j]
					ws[f"{df[2]}{b}"].value = t4[j]
					ws[f"{df[0]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
					ws[f"{df[1]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
					ws[f"{df[2]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
					
					b+=1

				elif(i==4):
					ws[f"{df[1]}{b}"].value = f5[j]
					ws[f"{df[2]}{b}"].value = t5[j]
					ws[f"{df[0]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
					ws[f"{df[1]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
					ws[f"{df[2]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
						
					b+=1

				elif(i==5):
					ws[f"{df[1]}{b}"].value = f6[j]
					ws[f"{df[2]}{b}"].value = t6[j]
					ws[f"{df[0]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
					ws[f"{df[1]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
					ws[f"{df[2]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
					
					b+=1

				elif(i==6):
					ws[f"{df[1]}{b}"].value = f7[j]
					ws[f"{df[2]}{b}"].value = t7[j]
					ws[f"{df[0]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
					ws[f"{df[1]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
					ws[f"{df[2]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
						
					b+=1

				elif(i==7):
					ws[f"{df[1]}{b}"].value = f8[j]
					ws[f"{df[2]}{b}"].value = t8[j]
					ws[f"{df[0]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
					ws[f"{df[1]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
					ws[f"{df[2]}{b}"].border = Border(top=thin, left=thin, right=thin, bottom=thin)
						
					b+=1




			
	except:
		import streamlit as st
		st.write("Uploaded file is not in correct format.")
		

from platform import python_version
ver = python_version()

if ver == "3.8.10":
	print("Correct Version Installed")
else:
	print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")


proj_octant_gui()






#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
