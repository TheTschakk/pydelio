from schnittpunkte import schnittp as sp
import numpy as np
#kd_1=[[0,np.pi/4,0,5*np.pi/4,0]]
#kd_2=[[0,np.pi/4,0,np.pi/4,0]]
kd_1=[[0,np.pi/4,0,6*np.pi/4,0]]
kd_2=[[0,np.pi/4,0,0*np.pi/4,0]]

SP=sp(kd_1,kd_2)
print(SP)
