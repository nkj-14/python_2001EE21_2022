

from datetime import datetime
start_time = datetime.now()

#Help https://youtu.be/H37f_x4wAC0
def octant_longest_subsequence_count():
###Code
    #importing libraries
    import pandas as pd


    #for data preprocessing read all data
    try:
        data = pd.read_excel("input_octant_longest_subsequence.xlsx")

    

    except:
        print("Something went wrong while opening the file or file is not found.")
        exit()


from platform import python_version
ver = python_version()

if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")


octant_longest_subsequence_count()






#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))