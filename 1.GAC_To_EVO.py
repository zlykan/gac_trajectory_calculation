# coding:utf-8
from os import utime
from math import * 
from dd_to_ddmm import dd_to_ddmm
import sys

def gac_to_evo(input_filename,output_filename):
    file_input = open(input_filename, "r")
    file_output = open(output_filename,'w')

    for line in file_input.readlines():

        data = line.split()  
        temp_time = float(data[1])
        temp_hour = int(temp_time)/10000
        temp_min = int(temp_time)/100 - temp_hour*100
        temp_sec = int(temp_time) - temp_hour*10000 - temp_min*100
        temp_ms = temp_time - int(temp_time)
        time_now = temp_hour*3600 + temp_min*60 + temp_sec + temp_ms
       
        temp_x = float(data[2])
        
        temp_y = float(data[3])
        
        temp_z = float(data[4])
        temp_q1 = float(data[8])
        temp_q2 = float(data[9])
        temp_q3 = float(data[10])
        temp_q0 = float(data[11])
        
        UTC_time = time_now
        UTM_x = temp_x
        UTM_y = temp_y
        UTM_z = temp_z
        q1 = temp_q1
        q2 = temp_q2
        q3 = temp_q3
        q0 = temp_q0

        file_output.write(str(UTC_time))
        file_output.write(' ')
        file_output.write(str(UTM_x))
        file_output.write(' ')
        file_output.write(str(UTM_y))
        file_output.write(' ')
        file_output.write(str(UTM_z))
        file_output.write(' ')
        file_output.write(str(q1))
        file_output.write(' ')
        file_output.write(str(q2))
        file_output.write(' ')
        file_output.write(str(q3))
        file_output.write(' ')
        file_output.write(str(q0))
        file_output.write('\n')

    file_input.close()
    file_output.close()

if __name__ == '__main__':
    file_input = sys.argv[1]
    data = file_input.split('_')
    file_output = './output_evo_'+data[2]
    gac_to_evo(file_input,file_output)
