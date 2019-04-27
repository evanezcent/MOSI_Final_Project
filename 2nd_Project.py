import turtle


M = 100
p = 0.3
v0 = 0
N = 10
dt = 1
vmax = 5
tmax = 100
tr = []

for i in range(10) :
    tr.append(turtle.Turtle())
    tr[i].up()
    tr[i].ht()

for j in range(10):
    tr[j].st()
    tr[j].setx(-200)
    tr[j].speed('slowest')
    tr[j].fd(400)
    print(tr[j].pos() - tr[j+1].pos()) 
    

