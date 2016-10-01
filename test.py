import math, microbit, random

adjust=lambda x: int(math.floor(x))

microbit.display.scroll(">>>", delay=100)
firebase=[5+random.randrange(4) for i in range(5)]

cube=[[(i,j,k),(i,k,j),(k,i,j)] for i in [-10, 10] for j in [-10, 10] for k in range(-10,11)]
cube=list(set(list(itertools.chain(*cube))))
cube=[(i[0], i[1], i[2]+10) for i in cube]

def rotate_3dpoint(p, angle, ax):
  r=[0, 0, 0]
  ca=math.cos(angle)
  sa=math.sin(angle)
  r[0]+=(ca+(1-ca)*ax[0]*ax[0])*p[0]
  r[0]+=((1-ca)*ax[0]*ax[1]-ax[2]*sa)*p[1]
  r[0]+=((1-ca)*ax[0]*ax[2]+ax[1]*sa)*p[2]
  r[1]+=((1-ca)*ax[0]*ax[1]+ax[2]*sa)*p[0]
  r[1]+=(ca+(1-ca)*ax[1]*ax[1])*p[1]
  r[1]+=((1-ca)*ax[1]*ax[2]-ax[0]*sa)*p[2]
  r[2]+=((1-ca)*ax[0]*ax[2]-ax[1]*sa)*p[0]
  r[2]+=((1-ca)*ax[1]*ax[2]+ax[0]*sa)*p[1]
  r[2]+=(ca+(1-ca)*ax[2]*ax[2])*p[2]
  return r

def rotate(obj, angle, axis):
  for n,i in enumerate(obj): obj[n] = rotate_3dpoint(i, angle, axis)

def rotcube(step):
  step=int(math.floor(step/5))
  global cube, grid
  rotate(cube, (0.6+0.5*math.sin(step/35))/35, (1,1,1))
  rotate(cube, (0.85+0.75*math.cos((step+7)/50))/30, (1,0,0))
  rotate(cube, (1.1+math.sin((step+43)/20))/30, (0,1,1))
  oldgrid=grid
  grid=[[0 for i in range(50)] for j in range(50)]
  tempvert=[tuple(j+23 for j in i) for i in cube]
  try:
    for i in tempvert: grid[int(i[0])][int(i[1])]=i[2]
  except: grid=oldgrid
  return grid

def fire():

  global firebase
  newbase=[]
  for i in firebase:
    if random.choice([0,1]): a=abs(i+math.floor(random.randrange(2)))
    else: a=abs(i-math.floor(random.randrange(2)))
    a=9 if a>9 else 0 if a<0 else a
    newbase.append(a)
  previousline=newbase
  firebase=newbase

  for i in range(5):
    actualline=[]
    for j in range(5):
      lvl=adjust((previousline[j]+previousline[j+1])/3)-1 if j==0 else adjust((previousline[j]+previousline[j-1])/3)-1 if j==4 else adjust((previousline[j-1]+previousline[j]+previousline[j+1])/3)-1
      if lvl<0:lvl=0
      actualline.append(lvl)
      microbit.display.set_pixel(j,4-i,lvl)
    previousline=actualline

while 1:
  fire()
  microbit.sleep(50)