# Import the necessary libraries
from PIL import Image
from numpy import asarray
import numpy as np
import cv2


img = Image.open('normal.jpg')
nd = np.array(img)
offset=int((nd.shape[0]-1)/5)
file=open("message.txt","r")
message =file.read()
length=len(message)
if length>=4 :   
    normal_chunk=int(length/4*8)
else:
    normal_chunk=int(length*8)
#print(normal_chunk)
print("The original string is : " + str(message))
# Converting String to binary
res = ''.join(format(ord(i), '08b') for i in message)


# printing result 
print("The string after binary conversion : " + res)
bits=[]
for i in res:
    if(i=='0'):
        bits.append(254)
    else:
        bits.append(255)
#print(bits)
x=0
y=0
z=0
count=0
for i in range(len(bits)):     
     if count%normal_chunk==0 and count!=0:
        x=x+offset
        y=0
        z=0
     else:
        if z%3==0 and z!=0:
            y=y+1
            z=0
     if bits[i]==255 and nd[x,y,z]%2==0:
         nd[x,y,z] = nd[x,y,z]+1
         #print(x,y,z,' ',nd[x,y,z]%2)
         z=z+1
         count=count+1
         continue 
     nd[x,y,z]=nd[x,y,z]&bits[i]
     #print(x,y,z,' ',nd[x,y,z]%2)
     z=z+1
     count=count+1
newimg=Image.fromarray(nd)
newimg.save('updated.jpg') 








#decryption
nd1 =nd
num_char=int(len(message))#this info must be given for the decryption.
length=num_char
if length>=4:
    normal_chunk=int(length/4*8)
    numchunk=5
else:
    normal_chunk=int(length)*8
    numchunk=1
offset=int((nd1.shape[0]-1)/5)
dec=[]
x=0
y=0
z=0
count=0
for i in range(numchunk):
    for j in range(normal_chunk):
        if count>(length*8):
            break
        if z%3==0 and z!=0:
            y=y+1
            z=0
        dec.append(nd1[x,y,z]%2)
        count=count+1
#print(x,y,z,' ',nd1[x,y,z]%2)
        z=z+1
    x=x+offset
    y=0
    z=0

    
pix_val=[]
sm=0
for i in range(len(dec)):
    if i%8==0 and i!=0:
        pix_val.append(sm)
        sm=0
    sm+=(2**(7-i%8))*dec[i]
pix_val.append(sm)
#print(pix_val)
# Using Naive Method 
result = "" 
for val in pix_val:
    result = result + chr(val) 
# Printing resultant string 

    print("Resultant string", result)





img1=Image.open('normal.jpg')
img2=Image.open('updated.jpg')
img1.show()
img2.show()
