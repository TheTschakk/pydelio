/*
Version 2.0
Changelog:
2.0:	Alles neu zusammengestückelt aus Dropbox überresten.
		Kommentiert.

Hinweise:
Alle einzel Teile müssen überprüft werden.
Abgleich mit anderen alten Versionen.
*/
/*
sudo g++ -Wall -o [output] [input.cpp]
*/
#include <iostream>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

int main();
void input();
void rechenloop();
float dichte(int z);
int roh_i_errechnen();

//-----------------Dichte
int dichte_runs = 0; //Wie oft wurde dichte() aufgerufen? (für roh_i nur ein mal berechnen)
int x = 8;			//Anzahl der Höhen bei denen Werte vorliegen
float z_i[8]={824,1542,3156,4396,5813,7474,9486,12109};		//Höhen 										input
float p_i[8]={925,850,700,600,500,400,300,200};		//Druck 												input
float t_i[8]={17.6,14.5,6,-3.1,-12.3,-25.5,-42.8,-59.9};		//Temperatur								input
float fi_i[8]={61,29,11,12,7,9.4,39,75};		//releative luft.											input
float roh_i[8];	//Dichte aus gegebenen Werten
float roh_z;
float z;		//höhe
//-----------------dunkelflug

int main()
{
	cout << "running" << endl;
	input();
	rechenloop();
	cout << "end" << endl;
	return 0;
}

void input(){
	cout << "start input" << endl;
	cout << "end input" << endl;
}

void rechenloop(){
	cout << "start rechenloop" << endl;

		float k1x;
        float k2x;
        float k3x;
        float k4x;

        float k1y;
        float k2y;
        float k3y;
        float k4y;

        float k1z;
        float k2z;
        float k3z;
        float k4z;

        float x;
        float dx;
        float vx; //v in x 						input
        float wvx; //Wind in x 					input

        float y;
        float dy;
        float vy;	// v in y					input
        float wvy; //wind in y 					input

        float z;  //Höhe 						input
        float dz; //							
        float vz; // 							input

        float w;  //Wiederstand                                   //Gamma*s/Gamma = s     ->Darg koefizient
        float S;  //querschnitt/masse Einsetzen   //berechnen
        float g = 9.81;   //Erdanziehung
        float rho = dichte(z); //dicht in abhängigkeit der höhe // erstmal konstant

        float vr;

        float schrittweite = dz; //höhenschritte

        while(z > 0){
                        /*k1 = f(xi, yi);
                k2 = f(xi+0,5*h , yi+0,5*k1*h);
                k3 = f(xi + 0,5*h, yi+0,5*k2*h);
                k4 = f(xi+h, yi+k3*h);

                xi+1 = yi+((1/6)*(k1+2*k2+2*k3+k4)*h;*/

                vr = sqrt(pow(vz,2)+pow((vx+wvx),2)+pow((vy+wvy),2));

                k1x = -w*S*rho*vr*(vx-wvx)/vz;
                k1y = -w*S*rho*vr*(vy-wvy)/vz;
                k1z = (-w*S*rho*vr*vz-g)/vz;

                k2x = -w*S*rho*(sqrt(pow((vx+0.5*k1x*dz-wvx),2)+pow((vy+0.5*k1y*dz-wvy),2)+pow((vz+0.5*k1z*dz),2))*(vx+0.5*k1x*dz-wvx))/(vz+0.5*k1z*dz);
                k2y = -w*S*rho*(sqrt(pow((vx+0.5*k1x*dz-wvx),2)+pow((vy+0.5*k1y*dz-wvy),2)+pow((vz+0.5*k1z*dz),2))*(vx+0.5*k1x*dz-wvx))/(vz+0.5*k1z*dz);
                k2z = (-w*S*rho*sqrt(pow((vx+0.5*k1x*dz-wvx),2)+pow((vy+0.5*k1y*dz-wvy),2)+pow((vz+0.5*k1z*dz),2))*(vz+0.5*k1z*dz)-g)/(Vz+0.5*k1z*dz);

                k3x = -w*S*sqrt(pow((vx+0.5*k2x*dz-wvx),2)+pow((vy+0.5*k2y*dz-wvy),2)+pow((vz+0.5k2z*dz),2))(vx+0.5*k2x*dz-wvx)/(vz+0.5*k2z*dz);
                k3y = -w*S*sqrt(pow((vx+0.5*k2x*dz-wvx),2)+pow((vy+0.5*k2y*dz-wvy),2)+pow((vz+0.5k2z*dz),2))(vx+0.5*k2x*dz-wvx)/(vz+0.5*k2z*dz);
                k3z = (-w*S*rho*sqrt(pow((vx+0.5*k2*dz-wvx),2)+pow((vy+0.5*k2y*dz-wvy),2)*pow((vz+0.5*k2z*dz),2))(vz+0.5*k2z*dz)-g)/(vz+0.5*k2z*dz);

                k4x = -w*S*sqrt(pow((vx+k3x*dz-wvx),2)+pow((vy+k3y*dz-wvy),2)+pow((vz+k3z*dz),2))*(vx+k3x*dz-wvx)/(vz+0.5*k3z*dz);
                k4y = -w*S*sqrt(pow((vx+k3x*dz-wvx),2)+pow((vy+k3y*dz-wvy),2)+pow((vz+k3z*dz),2))*(vx+k3x*dz-wvx)/(vz+0.5*k3z*dz);
                k4z = (-w*S*rho*sqrt(pow((vx+k3x*dz-wvx),2)+pow((vy+k3y*dz-wvy),2)+pow((vz+k3z*dz),2))*(vz+k3z*dz)-g)/(vz+k3z*dz);


                //änderung x
                vx = vx-((1/6)*(k1z+2*k2z+2*k3z+k4z)*dz;
                
                //änderung y
                vy = vy-((1/6)*(k1z+2*k2z+2*k3z+k4z)*dz;
                
                //änderung z
                vz = vz+((1/6)*(k1z+2*k2z+2*k3z+k4z)*dz;

                cout << "Höhe: " << z << endl;
        }

	cout << "end rechenloop" << endl;
}

float dichte(int z){
	if (dichte_runs == 0){
		roh_i_errechnen();
	}
	dichte++; 

	int u = 0;	//eigentlich 1 ?
	while(z > z_i[u]){
		u++;
	}
	roh_z = roh_i[u]*pow((roh_i[u+1]/roh_i[u]),((z-z_i[u])/(z_i[u+1]-z_i[u])));
	return roh_z;
	cout << "dichte für Höhe=" << z <<": " << rho_z << endl;
	return (rho_z) 
}

int roh_i_errechnen(){
		const float Rl = 287.058;
		const float Rd = 461.523;

		float pd;

		for (int i = 0; i < x; i++){
			pd = 6.1078*pow(10,((17.62*t_i[i])/(243.12+t_i[i])));												//Bei Magnus-Formel t_i == Celsius
			roh_i[i] = ((p_i[i]*0.001)/Rl*(t_i[i]+273.15))*(1.0-(fi_i[i]/100.0)*(pd/p_i[i])*(1.0-(Rl/Rd)));		//Hier muss in Kelvin umgerechnet werden.
			cout << z_i[i]<<" "<< t_i[i] << " " << p_i[i] << " " << roh_i[i] << endl;
		}
		return 0;
	}