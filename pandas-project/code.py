# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)


#Code starts here
bank=pd.DataFrame(bank_data)
categorical_var=bank.select_dtypes(include='object')
#print(categorical_var.head())
numerical_var=bank.select_dtypes(include='number')
#print(numerical_var.head())
banks=bank.drop(['Loan_ID'],axis=1)
print(banks.isnull().sum())
bank_mode=banks.mode()
for column in banks.columns:
    banks[column].fillna(banks[column].mode()[0], inplace=True)
#print(banks.head())
#print(banks.isnull().sum().values.sum())
avg_loan_amount=pd.pivot_table(banks,index=['Gender', 'Married', 'Self_Employed'],values='LoanAmount')
#print(avg_loan_amount)
loan_approved_se=banks[(banks['Self_Employed']=='Yes') & (banks['Loan_Status']=='Y')].shape[0]
loan_approved_nse=banks[(banks['Self_Employed']=='No') & (banks['Loan_Status']=='Y')].shape[0]
Loan_Status=614
percentage_se=loan_approved_se/Loan_Status*100
percentage_nse=loan_approved_nse/Loan_Status*100
#print(percentage_se,percentage_nse)
loan_term=banks['Loan_Amount_Term'].apply(lambda x:x/12)
big_loan_term=loan_term[loan_term>=25].shape[0]
#print(big_loan_term)
loan_groupby=banks.groupby('Loan_Status')
loan_groupby=loan_groupby['ApplicantIncome', 'Credit_History']
mean_values=loan_groupby.mean()
print(mean_values)


