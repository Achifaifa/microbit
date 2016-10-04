import math, microbit, random

adjust=lambda x: int(math.floor(x))

microbit.display.scroll(">>>", delay=100)
firebase=[5+random.randrange(4) for i in range(5)]

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