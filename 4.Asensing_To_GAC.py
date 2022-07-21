# coding:utf-8
from os import utime
from math import * 
from lonlat_to_utm import *
import sys
import csv


def daoyuan_to_gac(input_filename,output_filename):
    with open(input_filename, 'r') as f:
        reader = csv.reader(f)
        result = list(reader)
        num = len(result)
        file_output= open(output_filename,'w')
        i = 0	
        for i in range(1, num):
            #print(i)
            tmp_time = int(float(result[i][0]))%86400000
            #print("-----------------")
            tmp_utc_time = float(tmp_time/1000.0)-18.0

            UTC_h = int(tmp_utc_time/3600)
            UTC_m = int(tmp_utc_time - UTC_h*3600)/60
            UTC_s = int(tmp_utc_time - UTC_h*3600 -UTC_m*60)
            UTC_ms = tmp_utc_time - int(tmp_utc_time)
            UTC_now = UTC_h*10000 + UTC_m*100 + UTC_s + UTC_ms


            temp_lon = float(result[i][1])
            temp_lat = float(result[i][2])
            temp_alt = float(result[i][3])

            temp_Vnorth = float(result[i][4])
            temp_Veast = float(result[i][5])
            temp_Vup = float(result[i][6])

            temp_roll = float(result[i][9])
            temp_pitch = float(result[i][8])
            temp_yaw = -float(result[i][7])

            (temp_UTM_x,temp_UTM_y) = lonlat_to_utm(temp_lat,temp_lon)

            temp_roll_rad = math.radians(temp_roll)
            temp_pitch_rad = math.radians(temp_pitch)
            temp_yaw_rad = math.radians(temp_yaw)
            temp_q0 = math.cos(temp_yaw_rad/2)*math.cos(temp_pitch_rad/2)*math.cos(temp_roll_rad/2)-math.sin(temp_yaw_rad/2)*math.sin(temp_pitch_rad/2)*math.sin(temp_roll_rad/2)
            temp_q1 = math.cos(temp_yaw_rad/2)*math.sin(temp_pitch_rad/2)*math.cos(temp_roll_rad/2)-math.sin(temp_yaw_rad/2)*math.cos(temp_pitch_rad/2)*math.sin(temp_roll_rad/2)
            temp_q2 = math.sin(temp_yaw_rad/2)*math.sin(temp_pitch_rad/2)*math.cos(temp_roll_rad/2)+math.cos(temp_yaw_rad/2)*math.cos(temp_pitch_rad/2)*math.sin(temp_roll_rad/2)
            temp_q3 = math.sin(temp_yaw_rad/2)*math.cos(temp_pitch_rad/2)*math.cos(temp_roll_rad/2)+math.cos(temp_yaw_rad/2)*math.sin(temp_pitch_rad/2)*math.sin(temp_roll_rad/2)


            L_UTC_time = 0.0
            UTC_time = UTC_now
            UTM_x = temp_UTM_x
            UTM_y = temp_UTM_y
            UTM_z = temp_alt
            Lat = temp_lat
            Lon = temp_lon
            Alt = temp_alt
            q1 = temp_q1
            q2 = temp_q2
            q3 = temp_q3
            q0 = temp_q0
            Roll = temp_roll
            Pitch = temp_pitch
            Yaw = temp_yaw
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

    file_output.close()

if __name__ == '__main__':
    file_input = sys.argv[1]
    file_output = './output_gac_asensing.txt'
    daoyuan_to_gac(file_input,file_output)


