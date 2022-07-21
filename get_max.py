# coding:utf-8
from os import utime
from math import * 
from dd_to_ddmm import dd_to_ddmm
import sys

def get_max(input_filename):
    f =  open(input_filename,"r")
    line  = f.readline() 
    last_x = 0.0
    last_y = 0.0
    last_z = 0.0
    last_time = 0.0
    max_x = 0.0
    max_y = 0.0
    max_z = 0.0
    min_x = 0.0
    min_y = 0.0
    min_z = 0.0
    i = 0


    while line:

        data = line.split()  
        if len(data) != 22:
            line  = f.readline()
            continue

        temp_time = float(data[1])
        temp_hour = int(temp_time)/10000
        temp_min = int(temp_time)/100 - temp_hour*100
        temp_sec = int(temp_time) - temp_hour*10000 - temp_min*100
        temp_ms = temp_time - int(temp_time)
        time_now = temp_hour*3600 + temp_min*60 + temp_sec + temp_ms
        temp_Vx = float(data[15])
        temp_Vy = float(data[16])
        temp_Vz = float(data[17])
        if i == 0:
            last_x = temp_Vx
            last_y = temp_Vy
            last_z = temp_Vz
            last_time = time_now
            i = i+1
            line  = f.readline()
            continue
        now_x = temp_Vx
        now_y = temp_Vy
        now_z = temp_Vz
        now_time = time_now

        delt_x = now_x - last_x
        delt_y = now_y - last_y
        delt_z = now_z - last_z
        delt_time = now_time - last_time
        delt_ax = delt_x/delt_time
        delt_ay = delt_y/delt_time
        delt_az = delt_z/delt_time


        if delt_ax > max_x:
            max_x = delt_ax
        if delt_ax < min_x:
            min_x = delt_ax

        if delt_ay > max_y:
            max_y = delt_ay
        if delt_ay < min_y:
            min_y = delt_ay

        if delt_az > max_z:
            max_z = delt_az
        if delt_az < min_z:
            min_z = delt_az

        last_x = now_x
        last_y = now_y
        last_z = now_z
        last_time = now_time

        line  = f.readline()  

    print("max_x = ")
    print(max_x)
    print("min_x = ")
    print(min_x)


    print("max_y = ")
    print(max_y)
    print("min_y = ")
    print(min_y)


    print("max_z = ")
    print(max_z)
    print("min_z = ")
    print(min_z)
    f.close()

if __name__ == '__main__':
    input_file = sys.argv[1]

    gac_robosense_filename = input_file
 
    get_max(gac_robosense_filename)
