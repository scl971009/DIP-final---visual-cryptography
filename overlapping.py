import argparse
import random

from PIL import Image

def overlap(filename1, filename2):
    """Generates a (2,2) visual cryptography scheme."""
    first = Image.open(filename1)
    f_pixels = first.load()

    #first.save("first.png")
    
    second = Image.open(filename2)
    s_pixels = second.load()

    #second.save("second.png")

    fourth = Image.new("1", (int(first.size[0]), int(first.size[1])))
    four_pixels = fourth.load()

    for i in range(fourth.size[0]):
        for j in range(fourth.size[1]):
          if f_pixels[ i , j ] * s_pixels[ i , j ] == 0:
            four_pixels[i,j] = 0
          else:
            four_pixels[i ,j ] =1
    fourth.save("result_overlapping.png")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("IMAGE1", help="The image to discrypt - 1")
    parser.add_argument("IMAGE2", help="The image to discrypt - 2")
    args = parser.parse_args()

    overlap(args.IMAGE1, args.IMAGE2)
