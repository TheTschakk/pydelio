import numpy as np #Sachen importiern
from deltaT import deltaT
from interpol import interpol
from schnittpunkte import schnittp
fehler=0#varibeln intialliesieren
w=[1,0.5,0,-0.5,-1]
a=[np.zeros(2) for i in range(5)]
a=np.array(a)
kd1 = np.genfromtxt('./data/video0_20170721_000058_179.txt', delimiter='\t',skip_header=1)
kd2 = np.genfromtxt('./data/video1_20170721_000052_918.txt', delimiter='\t',skip_header=1)
for p in range(len(kd1)): #ins Bogenmaß umrechnen
    kd1[p][1]=360-kd1[p][1]
    kd1[p][1]=kd1[p][1]*np.pi/180
    kd1[p][3]=kd1[p][3]*np.pi/180
for p in range(len(kd2)):
    kd2[p][1]=360-kd2[p][1]
    kd2[p][1]=kd2[p][1]*np.pi/180
    kd2[p][3]=kd2[p][3]*np.pi/180
for qw in range(10):#10mal
    for i, Dt in enumerate(w):#die Werte in w als versatz testen
        kd2i=deltaT(kd2, Dt)#verstaz addieren
        kd1i,kd2i=interpol(kd1,kd2i)#mit versatz interpolieren
        if kd1i is None:
            fehler=np.inf
        else:
            sp=schnittp(kd1i,kd2i)#schnittpunkte der Geraden berechnen
            fehler=0
            for loop in range(len(sp[0])):
                fehler+=((sp[1][loop][0]-sp[0][loop][0])**2+(sp[1][loop][1]-sp[0][loop][1])**2+(sp[1][loop][2]-sp[0][loop][2])**2)#Abstand der Punkte berechnen
            feher= fehler/len(sp[0])
        a[i]=[Dt,fehler]#fehler in Array eintragen
    #print(a)
    h=min(a[:,1])#aus a und w neues w erstellen
    #print(h)
    b=a[:,1].tolist()
    j=b.index(h)
    #print(j)
    wn=[0,0,0,0,0]
    wn[2]=w[j]
    try:
        wn[4]=w[j+1]
    except IndexError:
        print("b")
        wn[4]=w[j]+0.25
    try:
        wn[0]=w[j-1]
    except IndexError:
        print("a")
        wn[0]=w[j]-0.25
    wn[1]=(wn[0]+wn[2])/2
    wn[3]=(wn[2]+wn[4])/2
    w=wn
    #print(w)
eDt=w[2]
#print(kd1)
#print(kd2)
print(eDt)
kd2i=deltaT(kd2, eDt)#verstaz addieren
kd1i,kd2i=interpol(kd1,kd2i)#mit versatz interpolieren
sp=schnittp(kd1i,kd2i) #Schnittpunkte ausrechnen
#print(kd1i)
#print(kd2i)
Ps=[]
for i in range(len(sp[0])):# durchschnitts punkt bestimmen
    x=(sp[0][i][0]+sp[1][i][0])/2
    y=(sp[0][i][1]+sp[1][i][1])/2
    z=(sp[0][i][2]+sp[1][i][2])/2
    t=kd1i[i][0]-kd1i[len(sp[0])-1][0]
    Ps.append([t,x,y,z])
print(Ps)
#np.savetxt("test.txt",Ps, delimiter='\t')
