from rich.table import Table
from rich.console import Console
import numpy as np,matplotlib.pyplot as plt

def dx_dt(t,x):

    V = 75 #cm³
    a = b = .2 #mL/s
    c = 50 #μg/mL

    return ((a*c)-(b*x))/V

def euler(a,b,f,n,c0):

    h = (b-a)/n
    x = a
    w = c0

    x_ = [x]
    y_ = [w]

    for _ in range(1,n+1):

        w = w+h*f(x,w)
        x = x+h

        x_.append(x)
        y_.append(w)

    return x_,y_

x,y = euler(0,900,dx_dt,30,0)

table = Table(title='Absorción de drogas en un órgano')
table.add_column('Tiempo (s)',justify='right')
table.add_column('Concentración (μg/cm³)',justify='right')

for t,c in zip(x,y):
    table.add_row(f'{t:.1f}',f'{c:.20f}')

Console().print(table)

plt.plot(np.array(x),np.array(y),linestyle='solid',color='midnightblue',linewidth=1)
plt.scatter(np.array(x),np.array(y),marker='x',c=np.array(x)-np.array(y),cmap='BuPu_r',linewidths=2,s=25,edgecolor="indigo")
plt.xlabel('Tiempo (s)',color='black',fontsize=20)
plt.ylabel('Concentración pancreática de fentanilo (μg/cm³)',color='black',fontsize=20)
plt.axhline(y=(45), color='red',linewidth=1,linestyle='solid',label='Concentración crítica (45 μg/cm³)')

plt.legend()
plt.grid()
plt.show()
