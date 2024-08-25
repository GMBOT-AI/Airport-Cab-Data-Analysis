import numpy as np
'''As the file name is taxis.csv so loading the file
using skip_header to ignore the extra headings and to make process faster'''
#we will be solving 5 Questions
'''Question 1:Calculate Mean speed of all rides
   Question 2:Calculate Total Number of rides in Feb month only
   Question 3:Calculate number of rides where tip is above $50
   Question 4:Calculate number of rides where dropoff was JKF Airport(the code of JKF AIRPORT is 2 in the sheet)
   the sheet is attached you can check .....Enjoy!
'''
taxi=np.genfromtxt('taxis.csv' , delimiter=',' , skip_header=True)

#For Question 1:
speed=taxi[:,7]/(taxi[:,8]/3600)#dividing by 3600 as to convert it to seconds
mean_spd=speed.mean()
print(mean_spd)

#For Question 2:
#As the pickup month is Feb so it will be 2 in digit
pickups=taxi[taxi[:,1] == 2 , 1]
print(pickups.shape[0])

#For Question 3:
tip=taxi[taxi[:,12] > 50 , 12]
print(tip.shape[0])


#For QUestion 4:
#As in the sheet the code for JKF Airport is 2 so
dropoff=taxi[taxi[:,6] == 2 , 6]
print(dropoff.shape[0])


