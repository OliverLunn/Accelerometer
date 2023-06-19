#import modules
import serial
import time
import matplotlib.pyplot as plt

ser = serial.Serial('COM8', 19200, timeout=None) #reading data from port "COM8"
time.sleep(0.01)

#empty arrays for data storage
data_pkz = []
data_avgz = []

for i in range(20):
    #reading a byte
    line = ser.readline()
    if line:
        string = line.decode() #convert byte data to unicode string
        string = string.replace(" ","") #remove all spaces from string
        pk_z = float(string[-7:])   
        avg_z = float(string[40:45])

        print("z-accleration: ", pk_z)
        #print("avg z-accleration: ", avg_z)

        data_pkz.append(pk_z) #append values to array "data_pkz and data_avgz"
        data_avgz.append(avg_z)

ser.close()

print(string)

#building plot
fig, (ax1,ax2) = plt.subplots(2)

ax1.plot(data_pkz, '.-')
ax1.set_ylabel('z-acceleration (g)')

ax2.plot(data_avgz, '.-')
ax2.set_xlabel('Time')
ax2.set_ylabel('Avg z-acceleration (g)')
ax1.grid()
ax2.grid()
plt.show()
