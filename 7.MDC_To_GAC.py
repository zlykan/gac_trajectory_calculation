# coding:utf-8
from os import utime
from math import * 
from lonlat_to_utm import *
import sys
import csv


def mdc_to_gac(input_filename,output_filename):
    with open(input_filename, 'r') as f:
        reader = csv.reader(f)
        result = list(reader)
        num = len(result)
        file_output= open(output_filename,'w')
        i = 0	
        for i in range(1, num):
            tmp_time_s = int(result[i][1])
            tmp_time_ns = int(result[i][2])*0.000000001
            L_temp_time = tmp_time_s + tmp_time_ns

            UTC_time = L_temp_time%86400
            UTC_time1 = UTC_time - 8*60*60
            UTC_h = int(UTC_time1/3600)
            UTC_m = int(UTC_time1 - UTC_h*3600)/60
            UTC_s = int(UTC_time1 - UTC_h*3600 -UTC_m*60)
            UTC_ms = UTC_time1 - int(UTC_time1)
            UTC_now = UTC_h*10000 + UTC_m*100 + UTC_s + UTC_ms


            temp_lon = int(result[i][9])*0.0000001
            temp_lat = int(result[i][10])*0.0000001

            temp_alt = int(result[i][11])*0.01

            temp_q1 = float(result[i][12])
            temp_q2 = float(result[i][13])
            temp_q3 = float(result[i][14])
            temp_q0 = float(result[i][15])
            temp_satellite_qua = int(result[i][22])
            temp_roll1 = atan2(2*(temp_q0*temp_q1+temp_q2*temp_q3),1-2*(temp_q1*temp_q1+temp_q2*temp_q2))
            temp_pitch1 = asin(2*(temp_q0*temp_q2-temp_q3*temp_q1))
            temp_yaw1 = atan2(2*(temp_q0*temp_q3+temp_q1*temp_q2),1-2*(temp_q2*temp_q2+temp_q3*temp_q3))


            temp_roll_deg = degrees(temp_roll1)
            temp_pitch_deg = degrees(temp_pitch1)
            temp_yaw_deg = degrees(temp_yaw1)
            (UTM_x,UTM_y) = lonlat_to_utm(temp_lat,temp_lon)



            L_UTC_time = L_temp_time
            UTC_time = UTC_now
            UTM_x = UTM_x
            UTM_y = UTM_y
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

    file_output.close()

if __name__ == '__main__':
    file_input = sys.argv[1]
    file_output = './output_gac_mdc.txt'
    mdc_to_gac(file_input,file_output)


