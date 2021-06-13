import random
from math import*
#s="424d36000300000000003600000028000000000100000001000001001800000000000000030000000000000000000000000000000000"
#s="424d36000600000000003600000028000000000200000001000001001800000000000000060000000000000000000000000000000000"
starting="424d36000c000000000036000000280000000002000000020000010018000000000000000c0000000000000000000000000000000000"
result=[]
for i in range(0,int(len(starting)/2)):
        result.extend([int(str(starting[2*i]+starting[2*i+1]),base=16)])
f=open("juliaset.bmp","wb")
rec=float(input("input the real part of the constant"))
imc=float(input("input the imagenary part of the constant"))
c=complex(rec,imc)
for i in range(0,512):
        for r in range(0,512):
                Im=i/128-2
                Re=r/128-2
                z=complex(Re,Im)
                v=0
                while(v<750)and(abs(z)<200):
                        z=z**2+c
                        v=v+4
                c1,c2,c3=0,0,0
                if v<255 :
                        c1=v
                        c2,c3=0,0
                if (v>=255) and (v<511) :
                        c1=255
                        c2=v-255
                        c3=0
                if v>=511 :
                        c1=255
                        c2=255
                        c3=v-510
                if(c3>255):
                        print(c3)
                        
                result.extend([c1,c2,c3])
f.write(bytes(result))
f.close()
print("fin")
                
