import math
import csv
data=[60,61,65,63,98,99,90,95,91,96]
n=len(data)
total=0
for x in data:
    total+=int(x)
mean=total/n


squarelist=[]
for number in data:
    a=float(number)-mean
    a=a**2
    squarelist.append(a)
sum=0
for i in squarelist:
    sum=sum+i
result=sum/n-1

standarddeviation=math.sqrt(result)
print(standarddeviation)
