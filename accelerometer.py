#import modules
import serial
import time
import matplotlib.pyplot as plt

ser = serial.Serial('COM8', 9600, timeout=None) #reading data from port "COM8"
time.sleep(0.01)

#empty arrays for data storage
data_pkz = []
data_avgz = []



def pk_acceleration(object, timescale):
    for i in range(timescale):
        #reading a byte
        line = ser.readline()
        if line:
            string = line.decode() #convert byte data to unicode string
            string = string.split()
            peak_z, avg_z = string[12], string[7]
            print("Peak z-acceleration: ", string[12])
            print("Average Accleration: ", string[7])
            
        ser.close()    
    return peak_z, avg_z


peak_z, avg_z = pk_acceleration(ser, 20)







