import turtle
import numpy as np

M = 100
p = 0.3
v0 = 0
N = 10
dt = 1
vmax = 5
tmax = 100
tr = []
v = 0


for i in range(10) :
    tr.append(turtle.Turtle())
    tr[i].up()
    tr[i].ht()
for t in range(tmax):
    for j in range(10):
        tr[j].st()
        tr[j].setx(-200)
        if (i == 0):
            d = 0
        else:
            d = tr[j].xcor() - tr[j-1].xcor()
        v = min(v+1, vmax)
        print(d)
        v = min(v,d)
        prob = np.random.choice(np.arange(0, 2), p=[0.7,0.3])
        v = max(0,prob)
        print(v)
        
        tr[j].speed(v)
        tr[j].fd(400)
    

