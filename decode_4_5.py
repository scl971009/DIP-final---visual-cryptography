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


def decode(filename1, filename2):
    """Generates a (2,2) visual cryptography scheme."""
    first = Image.open(filename1)
    s1_pixels = first.load()

    
    second = Image.open(filename2)
    s2_pixels = second.load()

    #third = Image.open(filename3)
    #s3_pixels = third.load()
    
    decode = Image.new("RGB", (int(first.size[0]/3), int(first.size[1]/3)))
    d_pixels = decode.load()

   # s1_pixels,s2_pixels,s3_pixels = distinguish_layer(s1_pixels,s2_pixels,s3_pixels)

    for i in range(decode.size[0]):
      for j in range(decode.size[1]):
          # get RGB value
          RGB=[0,0,0]

          for r in range(3):
            list1=[]

            value1=s1_pixels[i*3+2,j*3+2][r]
            value2=s2_pixels[i*3+2,j*3+2][r]

            for k in range(8):
              if (s1_pixels[i*3+k%3,j*3+k/3][r]!=value1) and (s2_pixels[i*3+k%3,j*3+k/3][r]!=value2):
                list1.append(k+1)

            RGB[r]=binary_decode(list1)

          d_pixels[i,j]=(RGB[0],RGB[1],RGB[2])
          #print(d_pixels[i,j])


              
            

    decode.save("result_4.png")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("IMAGE1", help="The image to discrypt - 1")
    parser.add_argument("IMAGE2", help="The image to discrypt - 2")
    #parser.add_argument("IMAGE3", help="The image to discrypt - 3")
    args = parser.parse_args()

    decode(args.IMAGE1, args.IMAGE2)
