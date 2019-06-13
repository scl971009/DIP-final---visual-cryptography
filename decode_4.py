import argparse
import random

from PIL import Image

def binary_decode(list_binary):
 
  num=0
 # print("in binary",list_binary)
  for k in list_binary:
    num = num + (1<<(k-1))
  #  print(k,binary_1<<(k-1),num)
  return num

def  distinguish_layer(s1_pixels,s2_pixels,s3_pixels):
    flag=[4,4,4]

    for r in range (3):
      if flag[0]==4:
        tmp=s1_pixels[2,2][r]

        for i in range(8):
          if s1_pixels[i/3,i%3][r]!=tmp:
            flag[0]=r
            break
        if flag[0]!=4:
          continue

      if flag[1]==4:
        tmp=s2_pixels[2,2][r]

        for i in range(8):
          if s2_pixels[i/3,i%3][r]!=tmp:
            flag[1]=r
            break
        if flag[1]!=4:
          continue

      if flag[2]==4:
        tmp=s3_pixels[2,2][r]

        for i in range(8):
          if s3_pixels[i/3,i%3][r]!=tmp:
            flag[2]=r
            break
        if flag[2]!=4:
          continue

   # print(flag)
    if flag[0]>flag[1]:
      s1_pixels,s2_pixels = s2_pixels,s1_pixels
      flag[0],flag[1] = flag[1],flag[0]

    if flag[1]>flag[2]:
      s2_pixels,s3_pixels = s3_pixels,s2_pixels
      flag[1],flag[2]=flag[2],flag[1]

    if flag[0]>flag[1]:
      s1_pixels,s2_pixels = s2_pixels,s1_pixels
      flag[0],flag[1]=flag[1],flag[0] 

#    print(flag)

    return s1_pixels,s2_pixels,s3_pixels

def decode(filename1, filename2,filename3):
    """Generates a (2,2) visual cryptography scheme."""
    first = Image.open(filename1)
    s1_pixels = first.load()

    #first.save("first.png")
    
    second = Image.open(filename2)
    s2_pixels = second.load()

    third = Image.open(filename3)
    s3_pixels = third.load()
    #second.save("second.png")
    
    decode = Image.new("RGB", (int(first.size[0]/3), int(first.size[1]/3)))
    d_pixels = decode.load()

    s1_pixels,s2_pixels,s3_pixels = distinguish_layer(s1_pixels,s2_pixels,s3_pixels)

    for i in range(decode.size[0]):
      for j in range(decode.size[1]):
          # list_R
          list1=[]

          value=s1_pixels[i*3+2,j*3+2][0]
          #print(value)
          for k in range(8):
            if s1_pixels[i*3+k%3,j*3+k/3][0]!=value:
              list1.append(k+1)
          #  print(s1_pixels[i*3+k%3,j*3+k/3][0])
          list_R=[]
          for x in list1:
            list_R.append(x)
          
          list1.clear()

          #print(list_R)

          # list_G

          value=s2_pixels[i*3+2,j*3+2][1]

          for k in range(8):
            if s2_pixels[i*3+k%3,j*3+k/3][1]!=value:
              list1.append(k+1)
 
          list_G=[]
          for x in list1:
            list_G.append(x)
          
          list1.clear()

              # list_B

          value=s3_pixels[i*3+2,j*3+2][2]

          for k in range(8):
            if s3_pixels[i*3+k%3,j*3+k/3][2]!=value:
              list1.append(k+1)
 
          list_B=[]
          for x in list1:
            list_B.append(x)
          
          list1.clear()
          #print(list_B)
          #print("listR=",list_R)
          #rint("listG=",list_G)
          #print("listB=",list_B)
          d_pixels[i,j]=(binary_decode(list_R),binary_decode(list_G),binary_decode(list_B))
          #print(d_pixels[i,j])


              
            

    decode.save("result_4.png")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("IMAGE1", help="The image to discrypt - 1")
    parser.add_argument("IMAGE2", help="The image to discrypt - 2")
    parser.add_argument("IMAGE3", help="The image to discrypt - 3")
    args = parser.parse_args()

    decode(args.IMAGE1, args.IMAGE2,args.IMAGE3)
