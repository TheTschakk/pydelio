import numpy as np#importieren der Module
import copy as c
def schnittp(kd1_i,kd2_i):
    kd1=c.deepcopy(kd1_i)
    kd2=c.deepcopy(kd2_i)
    
    #Kamera1 Darmstadt Gundernhausen
    Pos_a=[3842,52484,165]
    #Pos_a=[1,1,0]#Daten zum Testen
    #Pos_b=[-1,-1,0]
    #Kamera2 Worms Pfeddersheim
    Pos_b=[-32696,25851,118]

    sp=[[np.zeros(3) for y in range(len(kd1))] for x in range(2)]
    for n in range(len(kd1)):
        alpha_A=kd1[n][3]
        beta_A=kd1[n][1]

        alpha_B=kd2[n][3]
        beta_B=kd2[n][1]

        alpha=np.cos(alpha_A)*np.cos(beta_A)

        beta=np.cos(alpha_A)*np.cos(beta_B)

        gamma=np.cos(alpha_B)*np.sin(beta_B)

        delta=np.cos(alpha_A)*np.sin(beta_A)

        detB=-gamma*alpha*(delta*beta-alpha*gamma)
        detB-=delta*np.sin(alpha_B)*(alpha*np.sin(alpha_B)-delta*np.sin(alpha_B))
        detB-=beta*np.sin(alpha_A)*(alpha*np.sin(alpha_B)-beta*np.sin(alpha_A))
        detB+=alpha*np.sin(alpha_B)*(alpha*np.sin(alpha_B)-beta*np.sin(alpha_A))
        detB+=gamma*np.sin(alpha_A)*(gamma*np.sin(alpha_A)-delta*np.sin(alpha_B))
        detB+=beta*delta*(delta*beta-alpha*gamma)

        x0=Pos_b[0]-Pos_a[0]
        y0=Pos_b[1]-Pos_a[1]
        z0=Pos_b[2]-Pos_a[2]
	
        detB_1=+x0*alpha*(gamma*delta-alpha*gamma)
        detB_1+=z0*delta*(gamma*np.sin(alpha_A)-delta*np.sin(alpha_B))
        detB_1+=y0*np.sin(alpha_A)*(alpha*np.sin(alpha_B)-beta*np.sin(alpha_A))
        detB_1-=z0*alpha*(alpha*np.sin(alpha_B)-beta*np.sin(alpha_A))
        detB_1-=x0*np.sin(alpha_A)*(gamma*np.sin(alpha_A)-delta*np.sin(alpha_B))
        detB_1-=y0*delta*(delta*beta-alpha*gamma)
        
        t_B=detB_1/detB

        detA=-delta*beta*(alpha*gamma-delta*beta)
        detA-=gamma*np.sin(alpha_A)*(delta*np.sin(alpha_B)-gamma*np.sin(alpha_A))
        detA-=alpha*np.sin(alpha_B)*(beta*np.sin(alpha_A)-alpha*np.sin(alpha_B))
        detA+=beta*np.sin(alpha_A)*(beta*np.sin(alpha_A)-alpha*np.sin(alpha_B))
        detA+=delta*np.sin(alpha_B)*(delta*np.sin(alpha_B)-gamma*np.sin(alpha_A))
        detA+=alpha*gamma*(gamma*alpha-beta*delta)
        
        detA_1=+x0*beta*(gamma*alpha-beta*delta)
        detA_1+=z0*gamma*(delta*np.sin(alpha_B)-gamma*np.sin(alpha_A))
        detA_1+=y0*np.sin(alpha_B)*(beta*np.sin(alpha_A)-alpha*np.sin(alpha_B))
        detA_1-=z0*beta*(beta*np.sin(alpha_A)-alpha*np.sin(alpha_B))
        detA_1-=x0*np.sin(alpha_B)*(delta*np.sin(alpha_B)-gamma*np.sin(alpha_A))
        detA_1-=y0*gamma*(alpha*gamma-delta*beta)
        
        t_A=-detA_1/detA

        m_B=[np.cos(alpha_B)*np.sin(beta_B),np.cos(alpha_B)*np.cos(beta_B),np.sin(alpha_B)]
        m_A=[np.cos(alpha_A)*np.sin(beta_A),np.cos(alpha_A)*np.cos(beta_A),np.sin(alpha_A)]
        m_B=np.array(m_B)
        m_A=np.array(m_A)
        #print(m_A)
        #print(m_B)
        x_B=np.array(Pos_b)
        x_A=np.array(Pos_a)
      
        sp[0][n]=x_B+t_B*m_B
        sp[1][n]=x_A+t_A*m_A
    return sp
