
import pandas as pd  
hb=pd.read_csv("C:\h1b_kaggle.csv\h1b_kaggle.csv",nrows=5000)  #reading the csv file
df=hb    #having a data frame
print("The first 10 entries are\n\n",df.head(10))
print("The last 10 entries are\n",df.tail(10))
sdf=df[50:60]  #slicing the data frame for 50th employee to 59th and storing it in a sub dataframe
print("The job titles for employee number 50 to 59 are \n\n",sdf.JOB_TITLE)
#print(sdf)
print("The max wage among all the employees is \n\n",df.PREVAILING_WAGE.max())
print("The min wage among all the employees is \n\n",df.PREVAILING_WAGE.min())
print("The max wage among all the employees is \n\n",df.PREVAILING_WAGE.mean())
df1 =( pd.DataFrame({'YEAR': range(2015,2025,1), 'PREVAILING_WAGE':[df.PREVAILING_WAGE[i] for i in range(10)]})) #calculating correlation for first ten employees by varying year
print("The correlation value is\n\n",df1['YEAR'].corr(df1['PREVAILING_WAGE']))
print("The employees having full time job and wage above 150000 are \n\n",sdf[(sdf.PREVAILING_WAGE>150000) & (sdf.FULL_TIME_POSITION=='Y')])
