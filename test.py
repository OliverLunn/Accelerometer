#import modules
import serial
import time
import matplotlib.pyplot as plt

ser = serial.Serial('COM8', 9600, timeout=None) #reading data from port "COM8"
time.sleep(0.05)

#empty arrays for data storage
data_pkz = []
data_avgz = []

fig = plt.figure()
plt.ylim(-2,2)


for i in range(2):
    #reading a byte
    line = ser.readline()
    if line:
        string = line.decode() #convert byte data to unicode string
        #string = string.replace(" ","") #remove all spaces from string
        pk_z = float(string[-7:])   
        avg_z = float(string[40:45])

        print("z-accleration: ", pk_z)
        #print("avg z-accleration: ", avg_z)

        data_pkz.append(pk_z) #append values to array "data_pkz and data_avgz"
        data_avgz.append(avg_z)
        print(string)
        plt.clf()
        plt.xlabel('Time')
        plt.ylabel('z-acceleration (g)')
        plt.plot(data_pkz,'.-')
        plt.pause(0.01)

ser.close()

plt.show()


