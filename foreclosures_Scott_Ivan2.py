import os.path
import dateutil.parser
import datetime
import numpy as np
#import csv

   
# Get the directory name for data files
directory = os.path.dirname(os.path.abspath(__file__))  

type1='Single Family'
type2='Multi-Family'

#initialize the aggregators
lenders=[]
    # Open the file
filename = os.path.join(directory, '2014_Foreclosures.csv')
datafile = open(filename,'r')
for line in datafile:     
    regis, proptype,lender = line.split(',')
  
    if 'Bank of America' in lender:
            lenders+=[0]       
    if 'Wells Fargo Bank N.A.'in lender:
            lenders+=[1] 
    if 'JP Morgan Chase NA' in lender:
            lenders+=[2]       
    if 'Capital One'in lender:
            lenders+=[3] 
    if 'Ocwen Loan Servicing  LLC' in lender:
            lenders+=[4]       
    if 'Nationstar Mortgage LLC'in lender:
            lenders+=[5]  
        #Close that year's file
datafile.close()
    
# Plot on one set of axes.
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1,1)

y_values = [0.1, 0.3, 0.4, 0.2, 0.4, 0.2]
text_values = ["BofA", "WF", "Chase", "CO", "OW", "NS"]
x_values = np.arange(1, len(text_values) + 1, 1)

plt.bar(x_values, y_values, align='center')
# Decide which ticks to replace.
#new_ticks = ["word for " + str(y) if y != 0.3 else str(y) for y in y_values]
#plt.yticks(y_values, new_ticks)
plt.xticks(x_values, text_values)
#plt.barh(y_axis, x_values, align='center')
#plt.yticks(y_axis, y_values)
#fig, ax = plt.subplots(1,1) 
#ax.plot(x,y)
#plt.plot(x, y)
plt.hist(lenders)
ax.set_ylabel('Number of Foreclosures')
ax.set_title('Number of foreclosures for 6 leading banks')
plt.show()