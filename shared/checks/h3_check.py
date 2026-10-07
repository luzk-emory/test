import numpy as np
Y=np.array([[40,47,45],[50,51,58],[60,61,62]],float); G=[2,3,99]
rows=[];y=[]
for i in range(3):
    for t in range(3):
        x=np.zeros(1+2+2+1); x[0]=1
        if i>0: x[i]=1
        if t>0: x[2+t]=1
        x[5]=1.0 if t+1>=G[i] else 0.0
        rows.append(x); y.append(Y[i,t])
b=np.linalg.lstsq(np.array(rows),np.array(y),rcond=None)[0];print('TWFE',b[5])
