
import math


def dd_to_ddmm(input):
    dd = int(input)
    mm = (input - dd)*60
    ddmm = dd*100+mm

    return ddmm