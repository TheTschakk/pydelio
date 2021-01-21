import numpy as np
import copy as c
def deltaT(kd2_i,deltaT):
    kd2=c.deepcopy(kd2_i)
    for x in range(0,len(kd2)):
        kd2[x][0]=kd2[x][0]+deltaT
    return kd2



