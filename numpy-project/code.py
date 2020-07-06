# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
census=np.concatenate((data,new_record),axis=0)
age=census[:,0]
max_age=age.max()
min_age=age.min()
age_mean=age.mean()
age_std=np.std(age)
race0=census[:,2]==0
race_0=census[race0]
len_0=len(race_0)
race1=census[:,2]==1
race_1=census[race1]
len_1=len(race_1)
race2=census[:,2]==2
race_2=census[race2]
len_2=len(race_2)
race3=census[:,2]==3
race_3=census[race3]
len_3=len(race_3)
race4=census[:,2]==4
race_4=census[race4]
len_4=len(race_4)
mini=np.array([len_0,len_1,len_2,len_3,len_4])
minority_race=mini.argmin()
senior=census[:,0]>60
senior_citizens=census[senior]
working_hours=senior_citizens.sum(axis=0)
working_hours_sum=working_hours[6]
senior_citizens_len=len(senior_citizens)
avg_working_hours=working_hours_sum/senior_citizens_len
print(avg_working_hours)
gten=census[:,1]>10
high=census[gten]
lten=census[:,1]<=10
low=census[lten]
avg_high=high.mean(axis=0)
avg_pay_high=avg_high[7]
avg_low=low.mean(axis=0)
avg_pay_low=avg_low[7]


