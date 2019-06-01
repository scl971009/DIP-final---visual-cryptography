import argparse
import random

from PIL import Image

seq = [1, 2, 3, 4, 5, 6, 7, 8]

def binary(n):
	binary_1=1
	binary = [x for x in seq if (n>>(x-1))&binary_1 ]
	return binary

def get_random(list, n):
	#random.seed('DIP')
	ran = random.sample(list, n)
	return ran

def setk(k):
	if k == 1:
		return 0, 0
	if k == 2:
		return 1, 0
	if k == 3:
		return 2, 0
	if k == 4:
		return 0, 1
	if k == 5:
		return 1, 1
	if k == 6:
		return 2, 1
	if k == 7:
		return 0, 2
	if k == 8:
		return 1, 2
	if k == 9:
		return 2, 2


def encrypt(filename1, filename2, filename_s):
	original_share1 = Image.open(filename1)
	original_share1 = original_share1.convert("RGBA")
	original_s1_pixels = original_share1.load()

	original_share2 = Image.open(filename2)
	original_share2 = original_share2.convert("RGBA")
	original_s2_pixels = original_share2.load()

	secret = Image.open(filename_s)
	secret = secret.convert("RGBA")
	se_pixels = secret.load()

	share1 = Image.new("RGBA", (original_share1.size[0] * 3, original_share1.size[1] * 3))
	s1_pixels = share1.load()

	share2 = Image.new("RGBA", (original_share2.size[0] * 3, original_share2.size[1] * 3))
	s2_pixels = share2.load()

	for i in range(original_share1.size[0]):
		for j in range(original_share1.size[1]):
							
			
	share1.save("share1.png")
	share2.save("share2.png")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("IMAGE_SHARE_1", help="The image to share 1")
    parser.add_argument("IMAGE_SHARE_2", help="The image to share 2")
    parser.add_argument("IMAGE_SECRET", help="The image to hide")
    args = parser.parse_args()

    encrypt(args.IMAGE_SHARE_1, args.IMAGE_SHARE_2, args.IMAGE_SECRET)