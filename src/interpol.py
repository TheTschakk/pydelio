import numpy as np #numpy importieren
import copy as c
def interpol(kd1_i, kd2_i):#interpolations funktion
    kd2i=c.deepcopy(kd1_i)
    kd1=c.deepcopy(kd1_i)
    kd2=c.deepcopy(kd2_i)
    T=None
    tauof=None
    if kd1[0][0]<kd2[0][0]:
        for T in range(0,len(kd1)):
            if kd1[T][0]>=kd2[0][0]:# bestimmen des Versatz
                tauof=0
                T-=1
                break
    elif kd1[0][0]>kd2[0][0]:
        for tauof in range(0,len(kd2)):
            if tauof<=kd2[tauof][0]:
                T=0
                #tauof=tauof-1
                break
    else:
        T=0
        tauof=0
    if T is None or tauof is None:
        return (None,None)
    loopmax=min(len(kd2)-tauof,len(kd1)-T)-1
    #print(loopmax)
    #print(tauof)
    for loop in range(loopmax):#Interpolieren
        tau=loop+tauof
        kd2i[tau][1] = (kd2[tau][1]-kd2[tau+1][1])/(kd2[tau][0]-kd2[tau+1][0])*(-kd2[tau][0]+ kd1[T+loop][0])+kd2[tau][1]#sau lange interpolations Formel
        kd2i[tau][3] = (kd2[tau][3]-kd2[tau+1][3])/(kd2[tau][0]-kd2[tau+1][0])*(-kd2[tau][0]+ kd1[T+loop][0])+kd2[tau][3]#sau lange interpolations Formel
    return(kd1[T:T+loopmax-tauof],kd2i[tauof:loopmax])
