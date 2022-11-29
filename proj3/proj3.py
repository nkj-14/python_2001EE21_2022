
import os
import ntpath
import glob
import pandas as pd
import numpy as np
import datetime
from pathlib import Path 
from datetime import datetime 
import streamlit as st


start_time = datetime.now() 
print(start_time.strftime("%c"))

def write_timestamp_to_file(name): 
	# creating the csv writer 
	# storing current date and time
	current_date_time = datetime.now()
	print("\nCurrent System Time: ", current_date_time)
	file1 = open("methods_timestamp.csv", "a")  # append mode
	file1.write(name + ","+ str(current_date_time)+"\n")
	file1.close()

def duration_timestamp_to_file(name, duration):  
	file1 = open("methods_timestamp.csv", "a")  # append mode
	file1.write(name +   ","+str(duration)+"\n")
	file1.close()


def useful_values_u():
	data['Var_u\'']=data['std_u\'']=data['Skewness_u\'']=data['Kurtosis_u\'']=''

	data['u\'u\'']=round(data['u\'']**2,3)
	data.at[0,'Var_u\'']=round(data['u\'u\''].mean(),3) #variance
	u_std=round(data['u\''].std(),3)
	data.at[0,'std_u\'']=u_std                          #standard deviation
	data.at[0,'Skewness_u\'']=round(data['u\''].skew(),3)#skewness
	data.at[0,'Kurtosis_u\'']=round(data['u\''].kurt(),3)#kurtosis
	data['u^']=round(data['u\'']/u_std,3)

def useful_values_v():
	data['Var_v\'']=data['std_v\'']=data['Skewness_v\'']=data['Kurtosis_v\'']=''

	data['v\'v\'']=round(data['v\'']**2,3)
	data.at[0,'Var_v\'']=round(data['v\'v\''].mean(),3) #variance
	u_std=round(data['v\''].std(),3)
	data.at[0,'std_v\'']=u_std                          #standard deviation
	data.at[0,'Skewness_v\'']=round(data['v\''].skew(),3)#skewness
	data.at[0,'Kurtosis_v\'']=round(data['v\''].kurt(),3)#kurtosis
	data['v^']=round(data['v\'']/u_std,3)

def useful_values_w():
	data['Var_w\'']=data['std_w\'']=data['Skewness_w\'']=data['Kurtosis_w\'']=''

	data['w\'w\'']=round(data['w\'']**2,3)
	data.at[0,'Var_w\'']=round(data['w\'w\''].mean(),3) #variance
	w_std=round(data['w\''].std(),3)
	data.at[0,'std_w\'']=w_std                           #standard deviation
	data.at[0,'Skewness_w\'']=round(data['w\''].skew(),3)#skewness
	data.at[0,'Kurtosis_w\'']=round(data['w\''].kurt(),3)#kurtosis
	data['w^']=round(data['w\'']/w_std,3)

def useful_values():
	data['U_mean']=data['V_mean']=data['W_mean']=''
	U_mean=round(data['U'].mean(),3)
	V_mean=round(data['V'].mean(),3)
	W_mean=round(data['W'].mean(),3)

	data.at[index,'U_mean']=U_mean
	data.at[index,'V_mean']=V_mean
	data.at[index,'W_mean']=W_mean

	data['u\'']=round(data['U']-U_mean,3)
	data['v\'']=round(data['V']-V_mean,3)
	data['w\'']=round(data['W']-W_mean,3)
	N=data['U'].count()
	
	useful_values_u()
	useful_values_v()
	useful_values_w()
		
	data['Reynolds_stress_u\'v\'']=data['Reynolds_stress_u\'w\'']=data['Reynolds_stress_v\'w\'']=''
	
	data['u\'v\'']=data['u\'']*data['v\'']
	data.at[0,'Reynolds_stress_u\'v\'']=round(data['u\'v\''].mean(),3)
	
	data['u\'w\'']=data['u\'']*data['w\'']
	data.at[0,'Reynolds_stress_u\'w\'']=round(data['u\'w\''].mean(),3)
	
	data['v\'w\'']=data['v\'']*data['w\'']
	data.at[0,'Reynolds_stress_v\'w\'']=round(data['v\'w\''].mean(),3)
	
	data.at[0,'anisotropy']=round(data.at[0,'std_w\'']/data.at[0,'std_u\''],3)
	data['M30']=data['M03']=data['M12']=data['M21']=''

	data['u^u^w^']=round((data['u^']**2)*(data['w^']),3)
	data['u^w^w^']=round((data['w^']**2)*(data['u^']),3)
	data['u^u^u^']=round(data['u^']**3,3)
	data['w^w^w^']=round(data['w^']**3,3)
	
	data.at[0,'M21']=round(data['u^u^w^'].mean(),3)
	data.at[0,'M12']=round(data['u^w^w^'].mean(),3)
	data.at[0,'M30']=round(data['u^u^u^'].mean(),3)
	data.at[0,'M03']=round(data['w^w^w^'].mean(),3)

def fk():
	data['fku_2d']=data['Fku_2d']=data['fkw_2d']=data['Fkw_2d']=''
	data['u\'u\'u\'']=round(data['u\'']**3,3)
	data['u\'u\'u\' mean']=''
	data.at[0,'u\'u\'u\' mean']=round(data['u\'u\'u\''].mean(),3)

	data['u\'w\'w\'']=round((data['w\'']**2)*(data['u\'']),3)
	data['u\'w\'w\' mean']=''
	data.at[0,'u\'w\'w\' mean']=round(data['u\'w\'w\''].mean(),3)

	data['w\'w\'w\'']=round(data['w\'']**3,3)
	data['w\'w\'w\' mean']=''
	data.at[0,'w\'w\'w\' mean']=round(data['w\'w\'w\''].mean(),3)

	data['w\'u\'u\'']=round((data['u\'']**2)*(data['w\'']),3)
	data['w\'u\'u\' mean']=''
	data.at[0,'w\'u\'u\' mean']=round(data['w\'u\'u\''].mean(),3)

	data['u\'v\'v\'']=round((data['v\'']**2)*(data['u\'']),3)
	data['u\'v\'v\' mean']=''
	data.at[0,'u\'v\'v\' mean']=round(data['u\'v\'v\''].mean(),3)

	data['w\'v\'v\'']=round((data['v\'']**2)*(data['w\'']),3)
	data['w\'v\'v\' mean']=''
	data.at[0,'w\'v\'v\' mean']=round(data['w\'v\'v\''].mean(),3)

	constant_fk2d=input_1 
	multiplying_factor_3d=input_2 
	Shear_velocity=input_3

	data.at[index,'fku_2d']=round((data.at[0,'u\'u\'u\' mean']+data.at[0,'u\'w\'w\' mean'])*constant_fk2d,3)
	data.at[index,'Fku_2d']=round(data.at[index,'fku_2d']/Shear_velocity,3)

	data.at[index,'fkw_2d']=round((data.at[0,'w\'w\'w\' mean']+data.at[0,'w\'u\'u\' mean'])*constant_fk2d,3)
	data.at[index,'Fkw_2d']=round(data.at[index,'fkw_2d']/Shear_velocity,3)

	data['fku_3d']=data['Fku_3d']=data['fkw_3d']=data['Fkw_3d']=data['TKE_3d']=''

	data.at[index,'fku_3d']=round((data.at[0,'u\'u\'u\' mean']+ data.at[0,'u\'w\'w\' mean'] + data.at[0,'u\'v\'v\' mean'] )*multiplying_factor_3d,3)
	data.at[index,'Fku_3d']=round(data.at[index,'fku_2d']/Shear_velocity,3)

	data.at[index,'fkw_3d']=round((data.at[0,'w\'w\'w\' mean']+data.at[0,'w\'u\'u\' mean'] + data.at[0,'w\'v\'v\' mean'])*multiplying_factor_3d,3)
	data.at[index,'Fkw_3d']=round(data.at[index,'fkw_3d']/Shear_velocity,3)

	data.at[index,'TKE_3D']=round((data.at[0,'Var_v\'']*data.at[0,'Var_u\'']*data.at[0,'Var_w\''])* multiplying_factor_3d,3)

def Q_K_Value():
	data['Q1_K_Value']=data['Q2_K_Value']=data['Q3_K_Value']=data['Q4_K_Value']=''
	u_std=round(data['u\''].std(),3)
	w_std=round(data['w\''].std(),3)
	value=u_std*w_std
	X=10000
	k_first=k_second=k_third=k_fourth=0
	first=[0]*X
	second=[0]*X
	third=[0]*X
	fourth=[0]*X
	
	
	for i,row in data.iterrows():
		x=data.at[i,'u\'']*data.at[i,'w\'']
		if x<0:
			x=x*-1
			
		y=x/value
		z=int(y)
		if data.at[i,'u\'']>0 and data.at[i,'w\'']>0:
			first[z]=1
		if data.at[i,'u\'']<0 and data.at[i,'w\'']>0:
			second[z]=1
		if data.at[i,'u\'']<0 and data.at[i,'w\'']<0:
			third[z]=1
		if data.at[i,'u\'']>0 and data.at[i,'w\'']<0:
			fourth[z]=1
			
	for i in range(X):
		if first[X-i-1]!=0:
			data.at[index,'Q1_K_Value']=X-i
			break
			
	for i in range(X):
		if second[X-i-1]!=0:
			data.at[index,'Q2_K_Value']=X-i
			break
			
	for i in range(X):
		if third[X-i-1]!=0:
			data.at[index,'Q3_K_Value']=X-i
			break
			
	for i in range(X):
		if fourth[X-i-1]!=0:
			data.at[index,'Q4_K_Value']=X-i
			break

def octant_ID():
	data['Octant_id']=0
	for i in range(N):
		if data.at[i,'u\'']>=0 and data.at[i,'v\'']>=0:
			if data.at[i,'w\'']>=0:
				data.at[i,'Octant_id']=1
			if data.at[i,'w\'']<0:
				data.at[i,'Octant_id']=-1

		if data.at[i,'u\'']<0 and data.at[i,'v\'']>=0:
			if data.at[i,'w\'']>=0:
				data.at[i,'Octant_id']=2
			if data.at[i,'w\'']<0:
				data.at[i,'Octant_id']=-2

		if data.at[i,'u\'']<0 and data.at[i,'v\'']<0:
			if data.at[i,'w\'']>=0:
				data.at[i,'Octant_id']=3
			if data.at[i,'w\'']<0:
				data.at[i,'Octant_id']=-3

		if data.at[i,'u\'']>=0 and data.at[i,'v\'']<0:
			if data.at[i,'w\'']>=0:
				data.at[i,'Octant_id']=4
			if data.at[i,'w\'']<0:
				data.at[i,'Octant_id']=-4

def octant_column():
	data['Octant_plus_1']=data['Octant_minus_1']=''
	data['Octant_plus_2']=data['Octant_minus_2']=''
	data['Octant_plus_3']=data['Octant_minus_3']=''
	data['Octant_plus_4']=data['Octant_minus_4']=''
	data['Total_Octant_sample']=''

	data['Probability_Octant_plus_1']=data['Probability_Octant_minus_1']=''
	data['Probability_Octant_plus_2']=data['Probability_Octant_minus_2']=''
	data['Probability_Octant_plus_3']=data['Probability_Octant_minus_3']=''
	data['Probability_Octant_plus_4']=data['Probability_Octant_minus_4']=''

	data['Min_Octant_Count']=data['Min_Octant_Count_id']=''
	data['Max_Octant_Count']=data['Max_Octant_Count_id']=''

	data.at[index,'Min_Octant_Count']=data.at[index,'Min_Octant_Count_id']=N
	data.at[index,'Max_Octant_Count']=data.at[index,'Max_Octant_Count_id']=0

def max_min_update(i,j):
	if(data.at[index,'Min_Octant_Count']>i):
		data.at[index,'Min_Octant_Count']=i
		data.at[index,'Min_Octant_Count_id']=j
	if(data.at[index,'Max_Octant_Count']<i):
		data.at[index,'Max_Octant_Count']=i
		data.at[index,'Max_Octant_Count_id']=j

def octant():
	octant_ID()
	octant_column()
	
	# add all octant value with 4 to make it positive to store data in array
	# {-4,0},{-3,1},{-2,2},{-1,3},{NaN,4},{1,5},{2,6},{3,7},{4,8}
	octant_values_frequency=[0]*9 #array of size 9
	for i in range(N):
		x=data.at[i,'Octant_id']
		octant_values_frequency[x+4]+=1

	
	#for id 1
	data.at[index,'Octant_plus_1']=octant_values_frequency[1+4]
	data.at[index,'Probability_Octant_plus_1']=round(octant_values_frequency[1+4]/N,3)
	max_min_update(octant_values_frequency[1+4],1)

	#for id -1
	data.at[index,'Octant_minus_1']=octant_values_frequency[-1+4]
	data.at[index,'Probability_Octant_minus_1']=round(octant_values_frequency[-1+4]/N,3)
	max_min_update(octant_values_frequency[-1+4],-1)

	#for id 2
	data.at[index,'Octant_plus_2']=octant_values_frequency[2+4]
	data.at[index,'Probability_Octant_plus_2']=round(octant_values_frequency[2+4]/N,3)
	max_min_update(octant_values_frequency[2+4],2)

	#for id -2
	data.at[index,'Octant_minus_2']=octant_values_frequency[-2+4]
	data.at[index,'Probability_Octant_minus_2']=round(octant_values_frequency[-2+4]/N,3)
	max_min_update(octant_values_frequency[-2+4],-2)

	#for id 3
	data.at[index,'Octant_plus_3']=octant_values_frequency[3+4]
	data.at[index,'Probability_Octant_plus_3']=round(octant_values_frequency[3+4]/N,3)
	max_min_update(octant_values_frequency[3+4],3)

	#for id -3
	data.at[index,'Octant_minus_3']=octant_values_frequency[-3+4]
	data.at[index,'Probability_Octant_minus_3']=round(octant_values_frequency[-3+4]/N,3)
	max_min_update(octant_values_frequency[-3+4],-3)

	#for id 4
	data.at[index,'Octant_plus_4']=octant_values_frequency[4+4]
	data.at[index,'Probability_Octant_plus_4']=round(octant_values_frequency[4+4]/N,3)
	max_min_update(octant_values_frequency[4+4],4)

	#for id -4
	count_i=0
	data.at[index,'Octant_minus_4']=octant_values_frequency[-4+4]
	data.at[index,'Probability_Octant_minus_4']=round(octant_values_frequency[-4+4]/N,3)
	max_min_update(octant_values_frequency[-4+4],-4)
	
	#total octant
	data.at[index,'Total_Octant_sample']=N

def Acceleration_U():
	for i in range(N):
		if i==0:
			continue
		else:
			data.at[i,'accl_U']=(data.at[i,'U']-data.at[i-1,'U'])/data.at[1,'Time']
def Acceleration_V():
	for i in range(N):
		if i==0:
			continue
		else:
			data.at[i,'accl_V']=data.at[i,'V']-data.at[i-1,'V']/data.at[1,'Time']
def Acceleration_W():
	for i in range(N):
		if i==0:
			continue
		else:
			data.at[i,'accl_W']=data.at[i,'W']-data.at[i-1,'W']/data.at[1,'Time']
def update_acceleration():
	Acceleration_U()
	Acceleration_V()
	Acceleration_W()

def find_std():
	data['U_std']=data['V_std']=data['W_std']=0.0
	data.at[0,'U_std']=data['U'].std()
	data.at[0,'V_std']=data['V'].std()
	data.at[0,'W_std']=data['W'].std()   
def find_mean():
	data['U_mean']=data['V_mean']=data['W_mean']=0.0
	data.at[0,'U_mean']=data['U'].mean()
	data.at[0,'V_mean']=data['V'].mean()
	data.at[0,'W_mean']=data['W'].mean()


def replace_all_1(i):
	if i==0:
		return
	else:
		data.at[i,'U']=data.at[i-1,'U']
		data.at[i,'V']=data.at[i-1,'V']
		data.at[i,'W']=data.at[i-1,'W']
def replace_U_1(i):
	if i==0:
		return
	else:
		data.at[i,'U']=data.at[i-1,'U']
def replace_V_1(i):
	if i==0:
		return
	else:
		data.at[i,'V']=data.at[i-1,'V']
def replace_W_1(i):
	if i==0:
		return
	else:
		data.at[i,'W']=data.at[i-1,'W']


def replace_all_2(i):
	if i==0 or i==1:
		return
	else:
		data.at[i,'U']=2*data.at[i-1,'U']-data.at[i-2,'U']
		data.at[i,'V']=2*data.at[i-1,'V']-data.at[i-2,'V']
		data.at[i,'W']=2*data.at[i-1,'W']-data.at[i-2,'W']     
def replace_U_2(i):
	if i==0 or i==1:
		return
	else:
		data.at[i,'U']=2*data.at[i-1,'U']-data.at[i-2,'U']
def replace_V_2(i):
	if i==0 or i==1:
		return
	else:
		data.at[i,'V']=2*data.at[i-1,'V']-data.at[i-2,'V']
def replace_W_2(i):
	if i==0 or i==1:
		return
	else:
		data.at[i,'W']=2*data.at[i-1,'W']-data.at[i-2,'W']

def replace_all_3(i):
	if i==0:
		return
	data.at[i,'U']=data.at[0,'U_mean']
	data.at[i,'V']=data.at[0,'V_mean']
	data.at[i,'W']=data.at[0,'W_mean']
def replace_U_3(i):
	if i==0:
		return
	data.at[i,'U']=data.at[0,'U_mean']
def replace_V_3(i):
	if i==0:
		return
	data.at[i,'V']=data.at[0,'V_mean']
def replace_W_3(i):
	if i==0:
		return
	data.at[i,'W']=data.at[0,'W_mean']


def replace_all_4(i):
	if i<=12 or i>N-12:
		return
	else:
		x1=i-12
		y1=i
		x2=i+1
		y2=i+13
		data.at[i,'U']=(data['U'].iloc[x1:y1].mean()+data['U'].iloc[x2:y2].mean())/2
		data.at[i,'V']=(data['V'].iloc[x1:y1].mean()+data['V'].iloc[x2:y2].mean())/2
		data.at[i,'W']=(data['W'].iloc[x1:y1].mean()+data['W'].iloc[x2:y2].mean())/2
def replace_U_4(i):
	if i<12 or i>N-12:
		return
	else:
		x1=i-12
		y1=i
		x2=i+1
		y2=i+13
		data.at[i,'U']=(data['U'].iloc[x1:y1].mean()+data['U'].iloc[x2:y2].mean())/2
def replace_V_4(i):
	if i<12 or i>N-12:
		return
	else:
		x1=i-12
		y1=i
		x2=i+1
		y2=i+13
		data.at[i,'V']=(data['V'].iloc[x1:y1].mean()+data['V'].iloc[x2:y2].mean())/2
def replace_W_4(i):
	if i<12 or i>N-12:
		return
	else:
		x1=i-12
		y1=i
		x2=i+1
		y2=i+13
		data.at[i,'W']=(data['W'].iloc[x1:y1].mean()+data['W'].iloc[x2:y2].mean())/2


def replace_all_5(i):
	if i==0 or i==N-1:
		return
	else:
		data.at[i,'U']=(data.at[i-1,'U']+data.at[i+1,'U'])/2
		data.at[i,'V']=(data.at[i-1,'V']+data.at[i+1,'V'])/2
		data.at[i,'W']=(data.at[i-1,'W']+data.at[i+1,'W'])/2
def replace_U_5(i):
	if i==0 or i==N-1:
		return
	else:
		data.at[i,'U']=(data.at[i-1,'U']+data.at[i+1,'U'])/2
def replace_V_5(i):
	if i==0 or i==N-1:
		return
	else:
		data.at[i,'V']=(data.at[i-1,'V']+data.at[i+1,'V'])/2
def replace_W_5(i):
	if i==0 or i==N-1:
		return
	else:
		data.at[i,'W']=(data.at[i-1,'W']+data.at[i+1,'W'])/2


def replace_all(i,x):
	if(x==1):replace_all_1(i)
	if(x==2):replace_all_2(i)
	if(x==3):replace_all_3(i)
	if(x==4):replace_all_4(i)
	if(x==5):replace_all_5(i)

def replace_U(i,x):
	if(x==1):replace_U_1(i)
	if(x==2):replace_U_2(i)
	if(x==3):replace_U_3(i)
	if(x==4):replace_U_4(i)
	if(x==5):replace_U_5(i)

def replace_V(i,x):
	if(x==1):replace_V_1(i)
	if(x==2):replace_V_2(i)
	if(x==3):replace_V_3(i)
	if(x==4):replace_V_4(i)
	if(x==5):replace_V_5(i)
		
def replace_W(i,x):
	if(x==1):replace_W_1(i)
	if(x==2):replace_W_2(i)
	if(x==3):replace_W_3(i)
	if(x==4):replace_W_4(i)
	if(x==5):replace_W_5(i)

def acceleration_all_at_a_time_negative(x):
	found_peak=1
	max_iteration=12
	while found_peak and max_iteration>0:
		update_acceleration()
		find_std()
		find_mean()
		max_iteration-=1
		found_peak=0
		for i in range(N):
			if i==0:
				continue
			if (data.at[i,'accl_U']<-1*Lambda*g and data.at[i,'U']<-1*data.at[0,'U_std']*k) or(data.at[i,'accl_V']<-1*Lambda*g and data.at[i,'V']<-1*data.at[0,'V_std']*k) or (data.at[i,'accl_W']<-1*Lambda*g and data.at[i,'W']<-1*data.at[0,'W_std']*k):
				found_peak=1
				replace_all(i,x)

def acceleration_one_at_a_time_negative(x):
	found_peak=1
	max_iteration=12
	while found_peak and max_iteration>0:
		update_acceleration()
		find_std()
		find_mean()
		max_iteration-=1
		found_peak=0
		for i in range(N):
			if i==0:
				continue
			if ((data.at[i,'accl_U']*1)<-1*Lambda*g) and ((data.at[i,'U']*1)<(-1*data.at[0,'U_std']*k)):
				found_peak=1
				replace_U(i,x)
			if ((data.at[i,'accl_V']*1)<-1*Lambda*g)and ((data.at[i,'V']*1)<(-1*data.at[0,'V_std']*k)):
				found_peak=1
				replace_V(i,x)
			if  ((data.at[i,'accl_W']*1)<-1*Lambda*g) and ((data.at[i,'W']*1)<-1*data.at[0,'W_std']*k):
				found_peak=1
				replace_W(i,x) 

def acceleration_all_at_a_time_positive(x):
	found_peak=1
	max_iteration=12
	while found_peak and max_iteration>0:
		update_acceleration()
		find_std()
		find_mean()
		max_iteration-=1
		found_peak=0
		for i in range(N):
			if i==0:
				continue
			if (data.at[i,'accl_U']>1*Lambda*g and data.at[i,'U']>1*data.at[0,'U_std']*k) or(data.at[i,'accl_V']>1*Lambda*g and data.at[i,'V']>1*data.at[0,'V_std']*k) or (data.at[i,'accl_W']>1*Lambda*g and data.at[i,'W']>1*data.at[0,'W_std']*k):
				found_peak=1
				replace_all(i,x) 
		
def acceleration_one_at_a_time_positive(x):
	found_peak=1
	max_iteration=12
	while found_peak and max_iteration>0:
		update_acceleration()
		find_std()
		find_mean()
		max_iteration-=1
		found_peak=0
		for i in range(N):
			if i==0:
				continue
			if ((data.at[i,'accl_U']*1)>1*Lambda*g) and ((data.at[i,'U']*1)>(1*data.at[0,'U_std']*k)):
				found_peak=1
				replace_U(i,x) 
			if ((data.at[i,'accl_V']*1)>1*Lambda*g)and ((data.at[i,'V']*1)>(1*data.at[0,'V_std']*k)):
				found_peak=1
				replace_V(i,x) 
			if  ((data.at[i,'accl_W']*1)>1*Lambda*g) and ((data.at[i,'W']*1)>1*data.at[0,'W_std']*k):
				found_peak=1
				replace_W(i,x)

def update_acceleration_one_at_time(x):
	acceleration_one_at_a_time_negative(x)
	acceleration_one_at_a_time_positive(x)
	
def update_acceleration_all_at_time(x):
	acceleration_all_at_a_time_negative(x)
	acceleration_all_at_a_time_positive(x)

def Corr_All(x,corr):
	for i in range(N):
		if i==0:
			continue
		if int(data.at[i,'Corr_U'])<int(corr) or int(data.at[i,'Corr_V'])<int(corr) or int(data.at[i,'Corr_W'])<int(corr):
			replace_all(i,x)

def Corr_One(x,corr):
	for i in range(N):
		if i==0:
			continue
		if int(data.at[i,'Corr_U'])<int(corr):
			replace_U(i,x)
		if int(data.at[i,'Corr_V'])<int(corr):
			replace_V(i,x)
		if int(data.at[i,'Corr_W'])<int(corr):
			replace_W(i,x)

def SNR_All(x,SNR):
	for i in range(N):
		if i==0:
			continue
		if int(data.at[i,'SNR_U'])<int(SNR) or int(data.at[i,'SNR_V'])<int(SNR) or int(data.at[i,'SNR_W'])<int(SNR):
			replace_all(i,x)

def SNR_One(x,SNR):
	for i in range(N):
		if i==0:
			continue
		if int(data.at[i,'SNR_U'])<int(SNR):
			replace_U(i,x)
		if int(data.at[i,'SNR_V'])<int(SNR):
			replace_V(i,x)
		if int(data.at[i,'SNR_W'])<int(SNR):
			replace_W(i,x)
			


def store():
	with open(r"Results_v2.csv",mode='a') as file_:
		file_.write("{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}".format(name,data.at[0,'U_mean'],data.at[0,'V_mean'],data.at[0,'W_mean'],data.at[0,'Var_u\''],data.at[0,'Var_v\''],data.at[0,'Var_w\''],data.at[0,'std_u\''],data.at[0,'std_v\''],data.at[0,'std_w\''],data.at[0,'Skewness_u\''],data.at[0,'Skewness_v\''],data.at[0,'Skewness_w\''],data.at[0,'Kurtosis_u\''],data.at[0,'Kurtosis_v\''],data.at[0,'Kurtosis_w\''],data.at[0,'Reynolds_stress_u\'v\''],data.at[0,'Reynolds_stress_u\'w\''],data.at[0,'Reynolds_stress_v\'w\''],data.at[0,'anisotropy'],data.at[0,'M30'],data.at[0,'M03'],data.at[0,'M12'],data.at[0,'M21'],data.at[0,'fku_2d'],data.at[0,'Fku_2d'],data.at[0,'fkw_2d'],data.at[0,'Fkw_2d'],data.at[index,'fku_3d'],data.at[index,'Fku_3d'],data.at[index,'fkw_3d'],data.at[index,'Fkw_3d'],data.at[index,'TKE_3D'],data.at[0,'Q1_K_Value'],data.at[0,'Q2_K_Value'],data.at[0,'Q3_K_Value'],data.at[0,'Q4_K_Value'],0,0,data.at[0,'Octant_plus_1'],data.at[0,'Octant_minus_1'],data.at[0,'Octant_plus_2'],data.at[0,'Octant_minus_2'],data.at[0,'Octant_plus_3'],data.at[0,'Octant_minus_3'],data.at[0,'Octant_plus_4'],data.at[0,'Octant_minus_4'],data.at[0,'Total_Octant_sample'],data.at[0,'Probability_Octant_plus_1'],data.at[0,'Probability_Octant_minus_1'],data.at[0,'Probability_Octant_plus_2'],data.at[0,'Probability_Octant_minus_2'],data.at[0,'Probability_Octant_plus_3'],data.at[0,'Probability_Octant_minus_3'],data.at[0,'Probability_Octant_plus_4'],data.at[0,'Probability_Octant_minus_4'],data.at[0,'Min_Octant_Count'],data.at[0,'Min_Octant_Count_id'],data.at[0,'Max_Octant_Count'],data.at[0,'Max_Octant_Count_id'],"\n"))

def allfunction():
	useful_values()
	fk()
	Q_K_Value()
	octant()



def add_front_name(name,x):
	if(x==1):name = name + "_previous_point"
	if(x==2):name = name + "_2*last-2nd_last"
	if(x==3):name = name + "_overall_mean"
	if(x==4):name = name + "_12_point_strategy"
	if(x==5):name = name + "_mean_of_previous_2point"
	
	print(name)
	return name



st.markdown("<h1 style='text-align: center; color: grey;'>CS384 - Python</h1>", unsafe_allow_html=True)
	
st.markdown("<h2 style='text-align: center; color: black;'>Project 3</h2>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; color: black;'></h2>", unsafe_allow_html=True)

st.markdown("<h5 style='text-align: left; color: black;'>Kindly enter the input values for below:</h5>", unsafe_allow_html=True)

input_1 = st.number_input("constant_fk2d:")

st.markdown("<h3 style='text-align: center; color: black;'></h3>", unsafe_allow_html=True)
input_2 = st.number_input("multiplying_factor_3d:")		

st.markdown("<h3 style='text-align: center; color: black;'></h3>", unsafe_allow_html=True)

input_3 = st.number_input("Shear_velocity:")

st.markdown("<h3 style='text-align: center; color: black;'></h3>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: left; color: black;'>Filtering methods are as follows:</h5>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: left; color: black;'>1. C</h6>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: left; color: black;'>2. S</h6>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: left; color: black;'>3. A</h6>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: left; color: black;'>4. C & S</h6>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: left; color: black;'>5. C & A</h6>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: left; color: black;'>6. S & A</h6>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: left; color: black;'>7. C & S & A</h6>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: left; color: black;'>8. all combine</h6>", unsafe_allow_html=True)

input_4 = st.number_input("Choose filteribg method from above:", min_value=1, max_value=8, step=1)
st.markdown("<h3 style='text-align: center; color: black;'></h3>", unsafe_allow_html=True)
if(input_4==1):
	input_5=st.number_input("Enter thresold value C:", step=1)
elif(input_4==2):
	input_5=st.number_input("Enter thresold value S:", step=1)
elif(input_4==3):
	input_5 = st.number_input("Enter lambda value for A:")
	input_6 = st.number_input("Enter k value for A:", step=1)
elif(input_4==4):
	input_5 = st.number_input("Enter thresold value C:", step=1)
	input_6 = st.number_input("Enter thresold value S:", step=1)
elif(input_4==5):
	input_5 = st.number_input("Enter thresold value C:", step=1)
	input_6 = st.number_input("Enter lambda value for A:")
	input_7 = st.number_input("Enter k value for A:")
elif(input_4==6):
	input_5 = st.number_input("Enter thresold value S:", step=1)
	input_6 = st.number_input("Enter lambda value for A:")
	input_7 = st.number_input("Enter k value for A:")
elif(input_4==7 or input_4==8):
	input_5 = st.number_input("Enter thresold value C:", step=1)
	input_6 = st.number_input("Enter thresold value S:", step=1)
	input_7 = st.number_input("Enter lambda value for A:")
	input_8 = st.number_input("Enter k value for A:")

st.markdown("<h6 style='text-align: left; color: black;'>Replacement methods are as follows:</h6>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: left; color: black;'>1. previous point</h6>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: left; color: black;'>2. 2*last-2nd_last</h6>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: left; color: black;'>3. overall_mean</h6>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: left; color: black;'>4. 12_point_strategy</h6>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: left; color: black;'>5. mean of previous 2 point</h6>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: left; color: black;'>6. all seqential</h6>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: left; color: black;'>7. all parallel</h6>", unsafe_allow_html=True)

input_9 = st.number_input("Choose replacement method from above:", min_value=1, max_value=7,step=1)

#Adding buttons
st.markdown("<h2 style='text-align: center; color: black;'></h2>", unsafe_allow_html=True)
