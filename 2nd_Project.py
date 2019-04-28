import turtle
import numpy as np
import random as rd

M = 1000
p = 0.3
v0 = 0
N = 10
dt = 1
vmax = 50
tmax = 100
t = 0
tr = []
v = []
v = [v0]*N
vCar = []
clr = ['red','green','blue','black','yellow','orange','magenta','purple','pink','aquamarine']
koordinat =[]

for a in range(10):
    koordinat.append(rd.randint(-500,500))
koordinat.sort()

turtle.Screen().setup(1000,300,0,0)
turtle.Screen().delay(0)

def jarakMobil() :
    if (k == N-1):
        if(tr[k].xcor() > tr[0].xcor()):
           d = abs(M - (tr[i].xcor() - tr[0].xcor()))
           
        else :
           d = abs(tr[0].xcor() - tr[k].xcor())
           
    else :
        if (tr[k].xcor() < tr[k+1].xcor()) :
            d = abs(tr[k+1].xcor() - tr[k].xcor())
           
        else:
            d = abs(M - (tr[k+1].xcor() - tr[k].xcor()))
            
    return d
        
def updateV():
    v[k] = min(v[k]+1, vmax)
    d = jarakMobil()
    v[k] = min(v[k], d-5)
    x = np.random.uniform(0,1)
    if (x <= p):
        v[k] = max(0,v[k]-1)
    return v[k]


for j in range(10) :
    tr.append(turtle.Turtle())

for i in range (10) :
    tr[i].color(clr[i])
    tr[i].penup()
    tr[i].goto(koordinat[i],0)
    

while t <= tmax:
    for k in range(10):
        tr[k].forward(updateV())
        tr[k].speed(1)
        if (tr[k].xcor() >= 500):
            tr[k].ht()
            tr[k].goto(-500,0)
            tr[k].st()
    t+=1
    print(v)
    
    
    
        

