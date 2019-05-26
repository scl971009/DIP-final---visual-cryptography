import argparse
import random

from PIL import Image

def decode(filename1, filename2):
    """Generates a (2,2) visual cryptography scheme."""
    first = Image.open(filename1)
    f_pixels = first.load()

    #first.save("first.png")
    
    second = Image.open(filename2)
    s_pixels = second.load()

    #second.save("second.png")
    
    third = Image.new("1", (int(first.size[0]/3), int(first.size[1]/3)))
    t_pixels = third.load()

    for i in range(third.size[0]):
        for j in range(third.size[1]):
            count=0
            if  (f_pixels[3*i  , 3*j  ] * s_pixels[3*i  ,3*j  ])==0:
              count=count+1
            if  (f_pixels[3*i  , 3*j+1] * s_pixels[3*i  ,3*j+1])==0:
              count=count+1
            if  (f_pixels[3*i  , 3*j+2] * s_pixels[3*i  ,3*j+2])==0:
              count=count+1
            if  (f_pixels[3*i+1, 3*j  ] * s_pixels[3*i+1,3*j  ])==0:
              count=count+1
            if  (f_pixels[3*i+1, 3*j+1] * s_pixels[3*i+1,3*j+1])==0:
              count=count+1
            if  (f_pixels[3*i+1, 3*j+2] * s_pixels[3*i+1,3*j+2])==0:
              count=count+1
            if  (f_pixels[3*i+2, 3*j  ] * s_pixels[3*i+2,3*j  ])==0:
              count=count+1
            if  (f_pixels[3*i+2, 3*j+1] * s_pixels[3*i+2,3*j+1])==0:
              count=count+1
            if  (f_pixels[3*i+2, 3*j+2] * s_pixels[3*i+2,3*j+2])==0:
              count=count+1


            if count>=7:
            	t_pixels[i,j] = 0
            else:
                t_pixels[i,j] = 1

            

    third.save("result.png")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("IMAGE1", help="The image to discrypt - 1")
    parser.add_argument("IMAGE2", help="The image to discrypt - 2")
    args = parser.parse_args()

    decode(args.IMAGE1, args.IMAGE2)
