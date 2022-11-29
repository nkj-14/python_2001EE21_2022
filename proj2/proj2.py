
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
