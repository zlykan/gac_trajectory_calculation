# coding:utf-8
from os import utime
from math import * 
from lonlat_to_utm import *
import sys

def zhongdian_to_gac(input_filename,output_filename):
    file_input = open(input_filename, "r")
    file_output = open(output_filename,'w')

    temp_UTM_now = 0.0

    for line in file_input.readlines():

        data1 = line.split()  
        if len(data1)!= 4:
            # line  = file_input.readline()
            continue
        data = data1[3].split(',') 
        
        if(data[0] == '$GNGGA'):
            if len(data)!= 15:
                # line  = file_input.readline()
                continue
            # print(len(data))
            temp_UTM_now = float(data[1])
           #print(time_G)
            tem1 = int(float(data[2])*0.01)
            tem2 = (float(data[2]) - tem1*100)/60.0
            temp_lat = tem1 + tem2 
            tem1 = int(float(data[4])*0.01)
            tem2 = (float(data[4]) - tem1*100)/60.0
            temp_lon = tem1 + tem2 
            (temp_UTM_x,temp_UTM_y) = lonlat_to_utm(temp_lat,temp_lon)

            temp_satellite_qua = int(data[6])

            temp_alt = float(data[9])

        elif(data[0] == '$AUXINFO'):
            if len(data)!= 25:
                # line  = file_input.readline()
                continue
            # print(len(data))
            temp_UTM_now1 = float(data[1])
            #print(time_A)
            if (temp_UTM_now != temp_UTM_now1):
                # line  = file_input.readline()
                continue
            else :

                data3 = data[24].split('*') 
                temp_roll_origin =float(data[23]) 
                if temp_roll_origin > 180.0:
                    temp_roll_origin = temp_roll_origin - 360.0
                temp_pitch_origin =float(data[22])
                if temp_pitch_origin >180.0:
                    temp_pitch_origin =temp_pitch_origin - 360.0
                temp_yaw_origin=float(data3[0])
                if temp_yaw_origin > 180.0:
                    temp_yaw_origin = temp_yaw_origin - 360.0
                temp_roll = math.radians(temp_roll_origin)
                temp_pitch = math.radians(temp_pitch_origin)
                temp_yaw = math.radians(temp_yaw_origin)
                temp_q0 = math.cos(temp_yaw/2)*math.cos(temp_pitch/2)*math.cos(temp_roll/2)-math.sin(temp_yaw/2)*math.sin(temp_pitch/2)*math.sin(temp_roll/2)
                temp_q1 = math.cos(temp_yaw/2)*math.sin(temp_pitch/2)*math.cos(temp_roll/2)-math.sin(temp_yaw/2)*math.cos(temp_pitch/2)*math.sin(temp_roll/2)
                temp_q2 = math.sin(temp_yaw/2)*math.sin(temp_pitch/2)*math.cos(temp_roll/2)+math.cos(temp_yaw/2)*math.cos(temp_pitch/2)*math.sin(temp_roll/2)
                temp_q3 = math.sin(temp_yaw/2)*math.cos(temp_pitch/2)*math.cos(temp_roll/2)+math.cos(temp_yaw/2)*math.sin(temp_pitch/2)*math.sin(temp_roll/2)
                temp_Vel_E = float(data[18])
                temp_Vel_N = float(data[19])
                temp_Vel_U = float(data[20])
           
                L_UTC_time = 0.0
                UTC_time = temp_UTM_now1
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
                Roll = temp_roll_origin
                Pitch = temp_pitch_origin
                Yaw = temp_yaw_origin
                Vx_enu = temp_Vel_E
                Vy_enu = temp_Vel_N
                Vz_enu = temp_Vel_U
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
    file_output = './output_gac_kunchen.txt'
    zhongdian_to_gac(file_input,file_output)


