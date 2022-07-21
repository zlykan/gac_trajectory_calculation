# coding:utf-8
from os import utime
from math import * 
from lonlat_to_utm import *
import sys

def novetal_to_gac(input_filename,output_filename):
    file_input = open(input_filename, "r")
    file_output = open(output_filename,'w')

    for i in range(27):
        line = file_input.readline()
        print(line)
        continue

    for line in file_input.readlines():

        data = line.split()
        if (len(data)!= 10) and (len(data)!= 12):
            # line  = file_input.readline()
            continue

        data1 = data[0].split(':')
        temp_hour = int(data1[0])
        temp_min = int(data1[1])
        temp_sec = float(data1[2])
        temp_time = temp_hour*10000 + temp_min*100 + temp_sec

        temp_lat = float(data[1])
        temp_lon = float(data[2])
        temp_height = float(data[3])

        temp_Veast = float(data[4])
        temp_Vnorth = float(data[5])
        temp_Vup = float(data[6])

        temp_yaw_origin = -float(data[7])
        if temp_yaw_origin < -180 :
            temp_yaw_origin = temp_yaw_origin + 360
        temp_roll_origin = float(data[8])
        temp_pitch_origin = float(data[9])

        temp_roll = math.radians(temp_roll_origin)
        temp_pitch = math.radians(temp_pitch_origin)
        temp_yaw = math.radians(temp_yaw_origin)

        temp_q0 = math.cos(temp_yaw/2)*math.cos(temp_pitch/2)*math.cos(temp_roll/2)-math.sin(temp_yaw/2)*math.sin(temp_pitch/2)*math.sin(temp_roll/2)
        temp_q1 = math.cos(temp_yaw/2)*math.sin(temp_pitch/2)*math.cos(temp_roll/2)-math.sin(temp_yaw/2)*math.cos(temp_pitch/2)*math.sin(temp_roll/2)
        temp_q2 = math.sin(temp_yaw/2)*math.sin(temp_pitch/2)*math.cos(temp_roll/2)+math.cos(temp_yaw/2)*math.cos(temp_pitch/2)*math.sin(temp_roll/2)
        temp_q3 = math.sin(temp_yaw/2)*math.cos(temp_pitch/2)*math.cos(temp_roll/2)+math.cos(temp_yaw/2)*math.sin(temp_pitch/2)*math.sin(temp_roll/2)

        #(UTM_x,UTM_y) = lonlat_to_utm(float(data[2])*0.01,float(data[4])*0.01)
        (temp_UTM_x,temp_UTM_y) = lonlat_to_utm(temp_lat,temp_lon)

        L_UTC_time = 0.0
        UTC_time = temp_time
        UTM_x = temp_UTM_x
        UTM_y = temp_UTM_y
        UTM_z = temp_height
        Lat = temp_lat
        Lon = temp_lon
        Alt = temp_height
        q1 = temp_q1
        q2 = temp_q2
        q3 = temp_q3
        q0 = temp_q0
        Roll = temp_roll_origin
        Pitch = temp_pitch_origin
        Yaw = temp_yaw_origin
        Vx_enu = temp_Veast
        Vy_enu = temp_Vnorth
        Vz_enu = temp_Vup
        Wx = 0.0
        Wy = 0.0
        Wz = 0.0
        State = 0

        file_output.write(str(L_UTC_time))
        file_output.write(' ')
        file_output.write(str(UTC_time))
        file_output.write(' ')
        file_output.write(str(UTM_x))
        file_output.write(' ')
        file_output.write(str(UTM_y))
        file_output.write(' ')
        file_output.write(str(UTM_z))
        file_output.write(' ')
        file_output.write(str(Lat))
        file_output.write(' ')
        file_output.write(str(Lon))
        file_output.write(' ')
        file_output.write(str(Alt))
        file_output.write(' ')
        file_output.write(str(q1))
        file_output.write(' ')
        file_output.write(str(q2))
        file_output.write(' ')
        file_output.write(str(q3))
        file_output.write(' ')
        file_output.write(str(q0))
        file_output.write(' ')
        file_output.write(str(Roll))
        file_output.write(' ')
        file_output.write(str(Pitch))
        file_output.write(' ')
        file_output.write(str(Yaw))
        file_output.write(' ')
        file_output.write(str(Vx_enu))
        file_output.write(' ')
        file_output.write(str(Vy_enu))
        file_output.write(' ')
        file_output.write(str(Vz_enu))
        file_output.write(' ')
        file_output.write(str(Wx))
        file_output.write(' ')
        file_output.write(str(Wy))
        file_output.write(' ')
        file_output.write(str(Wz))
        file_output.write(' ')
        file_output.write(str(State))
        file_output.write('\n')

    file_input.close()
    file_output.close()
    

if __name__ == '__main__':
    file_input = sys.argv[1]
    file_output = './output_gac_novetal.txt'
    novetal_to_gac(file_input,file_output)


