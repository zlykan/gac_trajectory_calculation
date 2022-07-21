# coding:utf-8
from os import utime
from math import * 
from lonlat_to_utm import *
import sys


def robosense_to_gac(input_filename,output_filename):
    file_input = open(input_filename, "r")
    file_output = open(output_filename,'w')

    for line in file_input.readlines():
        
        data = line.split()  
        if(data[1]=='global_x') or (data[1]=='0'):
            # line  = file_input.readline()
            continue
        L_temp_time = float(data[0])
        UTC_time = L_temp_time%86400
        UTC_time1 = UTC_time - 8*60*60
        UTC_h = int(UTC_time1/3600)
        UTC_m = int(UTC_time1 - UTC_h*3600)/60
        UTC_s = int(UTC_time1 - UTC_h*3600 -UTC_m*60)
        UTC_ms = UTC_time1 - int(UTC_time1)
        UTC_now = UTC_h*10000 + UTC_m*100 + UTC_s + UTC_ms
    
        temp_lat = float(data[10])
        
        temp_lon = float(data[9])
        
        temp_alt = float(data[11])

        (temp_UTM_x,temp_UTM_y) = lonlat_to_utm(temp_lat,temp_lon)

        temp_roll_rad = 0.0
        temp_pitch_rad =0.0
        temp_yaw_rad = float(data[4])
        temp_roll_deg = math.degrees(temp_roll_rad)
        temp_pitch_deg = math.degrees(temp_pitch_rad)
        temp_yaw_deg = math.degrees(temp_yaw_rad)
        #print(temp_yaw_deg)
        temp_q0 = math.cos(temp_yaw_rad/2)*math.cos(temp_pitch_rad/2)*math.cos(temp_roll_rad/2)-math.sin(temp_yaw_rad/2)*math.sin(temp_pitch_rad/2)*math.sin(temp_roll_rad/2)
        temp_q1 = math.cos(temp_yaw_rad/2)*math.sin(temp_pitch_rad/2)*math.cos(temp_roll_rad/2)-math.sin(temp_yaw_rad/2)*math.cos(temp_pitch_rad/2)*math.sin(temp_roll_rad/2)
        temp_q2 = math.sin(temp_yaw_rad/2)*math.sin(temp_pitch_rad/2)*math.cos(temp_roll_rad/2)+math.cos(temp_yaw_rad/2)*math.cos(temp_pitch_rad/2)*math.sin(temp_roll_rad/2)
        temp_q3 = math.sin(temp_yaw_rad/2)*math.cos(temp_pitch_rad/2)*math.cos(temp_roll_rad/2)+math.cos(temp_yaw_rad/2)*math.sin(temp_pitch_rad/2)*math.sin(temp_roll_rad/2)
        
        # lon = dd_to_ddmm(temp_lon)
        # lat = dd_to_ddmm(temp_lat)
        temp_satellite_qua = int(data[8])


        L_UTC_time = L_temp_time
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
        Roll = temp_roll_deg
        Pitch = temp_pitch_deg
        Yaw = temp_yaw_deg
        Vx_enu = 0.0
        Vy_enu = 0.0
        Vz_enu = 0.0
        Wx = 0.0
        Wy = 0.0
        Wz = 0.0
        State = temp_satellite_qua
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
    file_output = './output_gac_robosense.txt'
    robosense_to_gac(file_input,file_output)


