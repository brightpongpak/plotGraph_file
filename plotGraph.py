import csv
import os
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as md
from datetime import datetime
from datetime import timedelta

listTime_open = []
listPm_open = []
listPm_close = []
listTime_close = []
date = ""
purifiersId = ""
map_Id = {}


print('Select Year and Mount:')
secDate = input()

listDir = []
[listDir.append(i) for i in os.listdir('../data')]

if(secDate not in listDir):
    print('Have no Date')
    exit()

print('List of purifiers:')
with open('../Data/purifiers.csv','r',encoding="utf8") as file:
    reader = csv.reader(file)
    header = next(reader)
    i = 1

    for line in reader:
        if(line[1] != header):
            print(line[1],"--> Number of device is : ",i)
            map_Id[str(i)] = line[0]
            i += 1
    


print('Select Air: ')
secpurifiers = input()

for key,valueOfkey in map_Id.items():
    if(secpurifiers == key):
        purifiersId = valueOfkey
        
if(purifiersId == ""):
    print('Have no device')
    exit()

with open('../Data2/'+secDate+'/'+secDate+'-'+purifiersId+'.csv','r') as file:
    reader = csv.reader(file)
    print('Select date:')
    date = input()
    realDate = secDate+date
    for line in reader:
        if(line[1] == realDate):
            if(line[3] == "1"):
                listPm_open.append(int(float(line[6])))
                listTime_open.append(datetime.strptime( realDate + line[2],"%Y%m%d%H%M"))
            else:
                listPm_close.append(int(float(line[6])))
                listTime_close.append(datetime.strptime(realDate + line[2],"%Y%m%d%H%M"))
        
    
titleDate = datetime.strptime(realDate,"%Y%m%d")   

plt.plot(listTime_open,listPm_open,'o',color = "green" , label='power on')    
plt.plot(listTime_close,listPm_close,'o',color ="red", label='power off')
plt.legend()
plt.xticks( rotation=25 )
ax=plt.gca()



list_Pm = listPm_close + listPm_open
if(len(list_Pm) == 0):
    print('No date in this date')
    exit()
else:
    if( 250 < max(list_Pm)):
        plt.axhspan(0, 12, color='green', alpha=0.5)
        plt.axhspan(12, 35, color='yellow', alpha=0.5)
        plt.axhspan(35, 55, color='orange', alpha=0.5)
        plt.axhspan(55, 150, color='red', alpha=0.5)
        plt.axhspan(150, 250, color='purple', alpha=0.5)
        plt.axhspan(250, 500, color='purple', alpha=0.5)
        
        

    elif( 150 <= max(list_Pm) < 251 ):
        plt.axhspan(0, 12, color='green', alpha=0.5)
        plt.axhspan(12, 35, color='yellow', alpha=0.5)
        plt.axhspan(35, 55, color='orange', alpha=0.5)
        plt.axhspan(55, 150, color='red', alpha=0.5)
        plt.axhspan(150, 250, color='purple', alpha=0.5)

    elif(55 <= max(list_Pm) < 151 ):
        plt.axhspan(0, 12, color='green', alpha=0.5)
        plt.axhspan(12, 35, color='yellow', alpha=0.5)
        plt.axhspan(35, 55, color='orange', alpha=0.5)
        plt.axhspan(55, 150, color='red', alpha=0.5)
        ax.set_ylim([0,150])
          
        

    elif(35 <= max(list_Pm) < 56 ):
        plt.axhspan(0, 12, color='green', alpha=0.5)
        plt.axhspan(12, 35, color='yellow', alpha=0.5)
        plt.axhspan(35, 55, color='orange', alpha=0.5)

    elif(12 <= max(list_Pm) < 36 ):
        plt.axhspan(0, 12, color='green', alpha=0.5)
        plt.axhspan(12, 35, color='yellow', alpha=0.5)
    else:
        plt.axhspan(0, 12, color='green', alpha=0.5)
        

xfmt = md.DateFormatter('%H')
ax.xaxis.set_major_formatter(xfmt)
plt.xlabel('Time')
plt.ylabel('PM2.5')

plt.title("ID of device is "+purifiersId+" "+titleDate.strftime("%A %d %B %Y"),fontsize="30",color='blue')
plt.show()

