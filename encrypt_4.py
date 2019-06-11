import argparse
import random

from PIL import Image

seq = [ 1, 2, 3, 4, 5, 6, 7, 8, 9]
mask= [ 1 ,   3,    5,    7,    9]

def binary_convert(n):
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

def encrypt(filename1,filename2,filename_s):
	original_share1 = Image.open(filename1)
	original_share1 = original_share1.convert("RGB")
	original_s1_pixels = original_share1.load()

	original_share2 = Image.open(filename2)
	original_share2 = original_share2.convert("RGB")
	original_s2_pixels = original_share2.load()

	secret = Image.open(filename_s)
	secret = secret.convert("RGB")
	se_pixels = secret.load()

	share1 = Image.new("RGB", (original_share1.size[0] * 3, original_share1.size[1] * 3))
	s1_pixels = share1.load()

	share2 = Image.new("RGB", (original_share2.size[0] * 3, original_share2.size[1] * 3))
	s2_pixels = share2.load()

	for i in range(original_share1.size[0]):
		for j in range(original_share1.size[1]):
			
			for r in range(3):


				s=binary_convert(se_pixels[i,j][r])

				if len(s)< 4: 
					bs=[x for x in seq if x not in s]
				else:
					bs=s
				
				bs1=get_random(bs, (int)(len(bs)/2))
				bs2=[x for x in bs if x not in bs1]

				if len(s)< 4: 
					for x in s: ##and 
						bs1.append(x)
						bs2.append(x)


				#for k in seq:

					#m,n=setk(k)
					#if (r==0):
					#	s1_pixels[i * 3 + m, j * 3 + n] 
					#	s2_pixels[i * 3 + m, j * 3 + n] 
					#if k in bs1:
					#	s1_pixels[i * 3 + m, j * 3 + n] + tuple(original_s1_pixels[i,j][r])
					#else:
					#	s1_pixels[i * 3 + m, j * 3 + n] + tuple(0)
					#if k in bs2:
					#	s2_pixels[i * 3 + m, j * 3 + n] + tuple(original_s2_pixels[i,j][r])
					#else:
					#	s2_pixels[i * 3 + m, j * 3 + n] + tuple(0)

							
			
	share1.save("share1_RGBA.png")
	share2.save("share2_RGBA.png")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("IMAGE_SHARE_1", help="The image to share 1")
    parser.add_argument("IMAGE_SHARE_2", help="The image to share 2")
    parser.add_argument("IMAGE_SECRET", help="The image to hide")
    args = parser.parse_args()

    encrypt(args.IMAGE_SHARE_1, args.IMAGE_SHARE_2, args.IMAGE_SECRET)