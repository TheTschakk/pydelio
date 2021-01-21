import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from numpy import genfromtxt

mdata=genfromtxt('test.txt',delimiter='\t')
mdata/=1000
mdata[:,0]*=1000
print(mdata)
poly_fitz=np.polyfit(mdata[:,1],mdata[:,3],2)


poly_fit=np.polyfit(mdata[:,1],mdata[:,2],2)
print(poly_fit)
poly_data=np.zeros((3,1000))
poly_data[0]=np.linspace(np.amin(mdata[:,1]),np.amax(mdata[:,1]),num=1000)
poly_data[1]=poly_fit[2]+poly_fit[1]*poly_data[0]+poly_fit[0]*poly_data[0]**2
fig = plt.figure()
poly_data[2]=poly_fitz[2]+poly_fitz[1]*poly_data[0]+poly_fitz[0]*poly_data[0]**2

ax = axes3d.Axes3D(fig)
ax.plot(mdata[:,1],mdata[:,2],'.',zs=0,zdir='z',color='r')
ax.plot(poly_data[0],poly_data[1],color='cyan')
ax.scatter(mdata[:,1], mdata[:,2], mdata[:,3],'.',color='b')
ax.scatter(poly_data[0],poly_data[1],poly_data[2],color='red')
plt.xlabel('X in km')
plt.ylabel('Y in km ')
ax.set_zlabel('Z in km')
plt.title('koordinaten Meteor')
plt.savefig('Plot.png',format='png')

plt.close()


fig = plt.figure()
plt.plot(mdata[:,0],mdata[:,1],'.')
plt.xlabel('t in s')
plt.ylabel('x in km ')

plt.savefig('Plot_tx.png',format='png')
plt.close()


fig = plt.figure()
plt.plot(mdata[:,0],mdata[:,3],'.')
plt.xlabel('t in s')
plt.ylabel('z in km ')
plt.savefig('Plot_tz.png',format='png')
plt.close()


fig = plt.figure()
plt.plot(mdata[:,0],mdata[:,2],'.')
plt.xlabel('t in s')
plt.ylabel('y in km ')
plt.savefig('Plot_ty.png',format='png')
plt.close()
