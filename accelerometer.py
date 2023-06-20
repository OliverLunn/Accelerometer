#import modules
import serial
import time
import matplotlib.pyplot as plt

def pk_acceleration(object):
    """
    This function reads data from RPi Pico accelerometer and outputs current
    peak z-acceleration reading.

    ----Input: ----
    Object: Reads data from RPi Pico

    ----Returns: ----
    peak_z [float] : Peak accleration measured. (Γ)
    
    """
    line = object.readline()
    if line:
        string = line.decode()
        string = string.split(',')
        peak_z = float(string[-1])

       
    return peak_z

def data_peak_z(timescale):
    """
    This function generates an array of peak z-acceleration values read over
    a chosen timescale. Calls function "pk_acceleration(object)" for peak 
    z-acceleration values.

    ----Input: ----
    timescale [int] : length of time data to be taken for

    ----Returns: ----
    data_peak_z [numpy array] : array of peak z-acceleration values
    """
    
    data_peak_z = []

    for i in range(timescale):
        peak_z = pk_acceleration(ser)
        data_peak_z.append(peak_z)

    ser.close() 
    return data_peak_z
  
ser = serial.Serial('COM8', 9600, timeout=None) #reading data from port "COM8"
time.sleep(0.01) 

#calling functions to generate peak z-acc values and array.
peak_z = pk_acceleration(ser)
print("Peak z-acceleration: ", peak_z)
data_peak_z = data_peak_z(20)

#plotting peak z-acc array
fig = plt.figure()
plt.xlabel('Time')
plt.ylabel('Peak z-acc ($\Gamma$)')
plt.plot(data_peak_z, '.-')
plt.grid()
plt.show()







