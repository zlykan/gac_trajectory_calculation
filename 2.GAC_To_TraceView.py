# coding:utf-8
from os import utime
from math import * 
from dd_to_ddmm import dd_to_ddmm
import sys

def gac_to_traceview(input_filename,output_filename):
    file_input = open(input_filename, "r")
    file_output = open(output_filename,'w')

    for line in file_input.readlines():

        data = line.split()  
        
        temp_time = float(data[1])
        temp_lat = float(data[5])       
        temp_lon = float(data[6])       
        temp_alt = float(data[7])
        temp_roll_deg = float(data[12])
        temp_pitch_deg = float(data[13])
        temp_yaw_deg = float(data[14])
        temp_Vx = float(data[15])
        temp_Vy = float(data[16])
        temp_Vz = float(data[17])
        temp_satellite_qua = int(data[21])

        if temp_yaw_deg < 0:
            temp_yaw_deg = temp_yaw_deg+360
        temp_yaw_deg1 = 360.0 - temp_yaw_deg
        temp_yaw_deg2 = temp_yaw_deg

        temp_speed = sqrt(temp_Vx*temp_Vx + temp_Vy*temp_Vy + temp_Vz*temp_Vz)*3.6

        utm_time = temp_time
        lat = dd_to_ddmm(temp_lat)
        lon = dd_to_ddmm(temp_lon)
        satellite_qua = temp_satellite_qua
        satellite_num = 0
        shuipingdu =0.0
        alt = temp_alt
        yaw_deg =temp_yaw_deg1
        chafenqixian = 0.0
        speed = temp_speed
        check_a = 16

        retain = 0.0
        cov_x = 0.0
        cov_y = 0.0
        cov_z = 0.0
        cov_Vx = 0.0
        cov_Vy = 0.0
        cov_Vz = 0.0
        cov_pitch = 0.0
        cov_roll = 0.0
        cov_yaw = 0.0
        Veast = temp_Vx
        Vnorth = temp_Vy
        Vz = temp_Vz
        pitch = temp_pitch_deg
        roll = temp_roll_deg
        yaw = temp_yaw_deg2
        check_b = 16

        file_output.write("$GNGGA")
        file_output.write(',')
        file_output.write(str(utm_time))
        file_output.write(',')
        file_output.write(str(lat))
        file_output.write(',')
        file_output.write('N')
        file_output.write(',')
        file_output.write(str(lon))
        file_output.write(',')
        file_output.write('E')
        file_output.write(',')
        file_output.write(str(satellite_qua))
        file_output.write(',')
        file_output.write(str(satellite_num))
        file_output.write(',')
        file_output.write(str(shuipingdu))
        file_output.write(',')
        file_output.write(str(alt))
        file_output.write(',')
        file_output.write('M')
        file_output.write(',')
        file_output.write(str(yaw_deg))
        file_output.write(',')
        file_output.write('M')
        file_output.write(',')
        file_output.write(str(chafenqixian))
        file_output.write(',')
        file_output.write(str(speed))
        file_output.write('*')
        file_output.write(str(check_a))
        file_output.write('\n')

        file_output.write("$AUXINFO")
        file_output.write(',')
        file_output.write(str(utm_time))
        file_output.write(',')
        file_output.write(str(retain))
        file_output.write(',')
        file_output.write(str(retain))
        file_output.write(',')
        file_output.write(str(retain))
        file_output.write(',')
        file_output.write('Vp')
        file_output.write(',')
        file_output.write(str(cov_x))
        file_output.write(',')
        file_output.write(str(cov_y))
        file_output.write(',')
        file_output.write(str(cov_z))
        file_output.write(',')
        file_output.write('Vv')
        file_output.write(',')
        file_output.write(str(cov_Vx))
        file_output.write(',')
        file_output.write(str(cov_Vy))
        file_output.write(',')
        file_output.write(str(cov_Vz))
        file_output.write(',')
        file_output.write('Va')
        file_output.write(',')
        file_output.write(str(cov_pitch))
        file_output.write(',')
        file_output.write(str(cov_roll))
        file_output.write(',')
        file_output.write(str(cov_yaw))
        file_output.write(',')
        file_output.write('V')
        file_output.write(',')
        file_output.write(str(Veast))
        file_output.write(',')
        file_output.write(str(Vnorth))
        file_output.write(',')
        file_output.write(str(Vz))
        file_output.write(',')
        file_output.write('A')
        file_output.write(',')
        file_output.write(str(pitch))
        file_output.write(',')
        file_output.write(str(roll))
        file_output.write(',')
        file_output.write(str(yaw))
        file_output.write('*')
        file_output.write(str(check_b))
        file_output.write('\n')
        
    file_input.close()
    file_output.close()

if __name__ == '__main__':
    file_input = sys.argv[1]
    data = file_input.split('_')
    file_output = './output_traceview_'+data[2]
    gac_to_traceview(file_input,file_output)
