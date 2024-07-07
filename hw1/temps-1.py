#Name: Connor Riley
#NetID: criley16
#HW1 Matplotlib, cosc370 summer 2024
#
from numpy import arange
import matplotlib.pyplot as plt
xData = arange(1,32)    # Ranges for x and y axes must match
tData = [86,87,84,86,86,86,84,83,90,89,88,85,86,79,83,81, \
         75,80,81,85,81,88,89,87,84,85,86,88,88,90,90]
avg = [86.]  # First value for montly avg high temp is just Day 1 temp

## 1) CALCULATE A RUNNING MONTHLY AVERAGE AND PRINT IT OUT IN A TABLE
##    IT DOES NOT MATTER HOW THE TABLE IS FORMATTED

#calculated the avg temps and appended them on the avg list
#accomplished via a for loop keeping a running total of temps
#until that day and dividing it by amount of days at that point
#then printed out in a nice list to 2 decimal places of accuracy 
temp_total = 0 #initialize var
for i in range(len(tData)):
  temp_total += tData[i] #calculate temp total
  if i > 0: #first entry already exists
    temp_avg = temp_total / (i+1) #avg calculation
    avg.append(temp_avg) #append to list
print('Day | Avg Temp')#print out avg values
print('--------------')
for i in range(len(avg)):
  if (i + 1) < 10:
    print(f'{i+1}   | {avg[i]:.2f}')
  else:
    print(f'{i+1}  | {avg[i]:.2f}')
  

## 2) CREATE A GRAPH FOR THE DATA USING MATPLOTLIB
##	- PLOT RED POINTS WITH BLUE LINE FOR ORIGINAL DATA -- DONE lines 54,55
##	- SHOW CHANGE IN AVERAGE HIGH WITH GREEN DASHED LINE -- DONE line 56
##	- SET DISPLAY RANGES FOR X AND Y AXES -- DONE lines 57,58
##		- X SHOULD RANGE FROM 0 TO 32 -- DONE line 57
##		- Y SHOULD RANGE FROM 70 TO 95 -- DONE line 58
##	- ENABLE GRID DISPLAY -- DONE line 62
##	- LABEL AXES AND SET TITLE -- DONE lines 59,60,61
##	- USE MATPLOTLIB.PYPLOT.TEXT() TO LABEL THE MONTHLY AVERAGE LINE --DONE line 63

#This section makes the plot, i first assign variables for the 
#graph data. then i plot the red circular markers first, then the
#blue solid line to have on top of the red markers. I then plot
#a dashed green line for the avg temp.I set x and y axis range
#I labeled the axis and titled the graph. I added a dashed grid
#for both the x and y coordinates. Lastly i add in text to label
#the avg temp line 
xPoints = xData
yPoints = tData
avgPoints = avg
plt.plot(xPoints, yPoints, 'ro') # red markers
plt.plot(xPoints, yPoints, 'b-') #blue line
plt.plot(xPoints, avgPoints, 'g--')#avg green dashed line
plt.xlim(0,32)#x axis range 
plt.ylim(70,95)#y axis range
plt.title("High Temperatures for Knoxville, TN - August 2013")#title
plt.xlabel('Day')#x axis name
plt.ylabel('High Temp')# y axis name
plt.grid(linestyle = '--')#grid
plt.text(15, 86, 'Monthly Avg', color='g')#text for green line
plt.show()

