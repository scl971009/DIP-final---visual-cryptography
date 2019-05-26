import argparse
import random

from PIL import Image

seq = [1, 2, 3, 4, 5, 6, 7, 8, 9]

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
	original_s1_pixels = original_share1.load()

	original_share2 = Image.open(filename2)
	original_s2_pixels = original_share2.load()

	secret = Image.open(filename_s)
	se_pixels = secret.load()

	share1 = Image.new("1", (original_share1.size[0] * 3, original_share1.size[1] * 3))
	s1_pixels = share1.load()

	share2 = Image.new("1", (original_share2.size[0] * 3, original_share2.size[1] * 3))
	s2_pixels = share2.load()

	for i in range(original_share1.size[0]):
		for j in range(original_share1.size[1]):
			if original_s1_pixels[i, j] != 0 and original_s2_pixels[i, j] !=0 and se_pixels[i, j] != 0:
				bc = get_random(seq, 4)
				wc = [x for x in seq if x not in bc]
				bb = get_random(bc, 3)
				wb = [x for x in seq if x not in bb]
				for k in bb:
					m, n = setk(k)
					s1_pixels[i * 3 + m, j * 3 + n] = 0
				for k in wb:
					m, n = setk(k)
					s1_pixels[i * 3 + m, j * 3 + n] = 1
				for k in bc:
					m, n = setk(k)
					s2_pixels[i * 3 + m, j * 3 + n] = 0
				for k in wc:
					m, n = setk(k)
					s2_pixels[i * 3 + m, j * 3 + n] = 1
			elif original_s1_pixels[i, j] != 0 and original_s2_pixels[i, j] != 0 and se_pixels[i, j] == 0:
				bc = get_random(seq, 4)
				wc = [x for x in seq if x not in bc]
				bb = get_random(wc, 3)
				wb = [x for x in seq if x not in bb]
				for k in bb:
					m, n = setk(k)
					s1_pixels[i * 3 + m, j * 3 + n] = 0
				for k in wb:
					m, n = setk(k)
					s1_pixels[i * 3 + m, j * 3 + n] = 1
				for k in bc:
					m, n = setk(k)
					s2_pixels[i * 3 + m, j * 3 + n] = 0
				for k in wc:
					m, n = setk(k)
					s2_pixels[i * 3 + m, j * 3 + n] = 1
			elif original_s1_pixels[i, j] == 0 and original_s2_pixels[i, j] !=0 and se_pixels[i, j] != 0:
				bb = get_random(seq, 6)
				wb = [x for x in seq if x not in bb]
				bc = get_random(bb, 3)
				wc = [x for x in seq if x not in bc]
				for k in bb:
					m, n = setk(k)
					s1_pixels[i * 3 + m, j * 3 + n] = 0
				for k in wb:
					m, n = setk(k)
					s1_pixels[i * 3 + m, j * 3 + n] = 1
				for k in bc:
					m, n = setk(k)
					s2_pixels[i * 3 + m, j * 3 + n] = 0
				for k in wc:
					m, n = setk(k)
					s2_pixels[i * 3 + m, j * 3 + n] = 1
			elif original_s1_pixels[i, j] == 0 and original_s2_pixels[i, j] !=0 and se_pixels[i, j] == 0:
				bb = get_random(seq, 6)
				wb = [x for x in seq if x not in bb]
				bc = get_random(wb, 3)
				wc = [x for x in seq if x not in bc]
				for k in bb:
					m, n = setk(k)
					s1_pixels[i * 3 + m, j * 3 + n] = 0
				for k in wb:
					m, n = setk(k)
					s1_pixels[i * 3 + m, j * 3 + n] = 1
				for k in bc:
					m, n = setk(k)
					s2_pixels[i * 3 + m, j * 3 + n] = 0
				for k in wc:
					m, n = setk(k)
					s2_pixels[i * 3 + m, j * 3 + n] = 1
			elif original_s1_pixels[i, j] != 0 and original_s2_pixels[i, j] == 0 and se_pixels[i, j] != 0:
				bc = get_random(seq, 6)
				wc = [x for x in seq if x not in bc]
				bb = get_random(bc, 3)
				wb = [x for x in seq if x not in bb]
				for k in bb:
					m, n = setk(k)
					s1_pixels[i * 3 + m, j * 3 + n] = 0
				for k in wb:
					m, n = setk(k)
					s1_pixels[i * 3 + m, j * 3 + n] = 1
				for k in bc:
					m, n = setk(k)
					s2_pixels[i * 3 + m, j * 3 + n] = 0
				for k in wc:
					m, n = setk(k)
					s2_pixels[i * 3 + m, j * 3 + n] = 1
			elif original_s1_pixels[i, j] != 0 and original_s2_pixels[i, j] == 0 and se_pixels[i, j] == 0:
				bc = get_random(seq, 6)
				wc = [x for x in seq if x not in bc]
				bb = get_random(wc, 3)
				wb = [x for x in seq if x not in bb]
				for k in bb:
					m, n = setk(k)
					s1_pixels[i * 3 + m, j * 3 + n] = 0
				for k in wb:
					m, n = setk(k)
					s1_pixels[i * 3 + m, j * 3 + n] = 1
				for k in bc:
					m, n = setk(k)
					s2_pixels[i * 3 + m, j * 3 + n] = 0
				for k in wc:
					m, n = setk(k)
					s2_pixels[i * 3 + m, j * 3 + n] = 1
			elif original_s1_pixels[i, j] == 0 and original_s2_pixels[i, j] == 0 and se_pixels[i, j] != 0:
				bb = get_random(seq, 6)
				wb = [x for x in seq if x not in bb]
				for k in bb:
					m, n = setk(k)
					s1_pixels[i * 3 + m, j * 3 + n] = 0
					s2_pixels[i * 3 + m, j * 3 + n] = 0
				for k in wb:
					m, n = setk(k)
					s1_pixels[i * 3 + m, j * 3 + n] = 1
					s2_pixels[i * 3 + m, j * 3 + n] = 1					
			else:
				bb = get_random(seq, 6)
				wb = [x for x in seq if x not in bb]
				bc = get_random(bb, 3)
				for x in wb:
					bc.append(x)
				wc = [x for x in seq if x not in bc]
				for k in bb:
					m, n = setk(k)
					s1_pixels[i * 3 + m, j * 3 + n] = 1
				for k in wb:
					m, n = setk(k)
					s1_pixels[i * 3 + m, j * 3 + n] = 0
				for k in bc:
					m, n = setk(k)
					s2_pixels[i * 3 + m, j * 3 + n] = 1
				for k in wc:
					m, n = setk(k)
					s2_pixels[i * 3 + m, j * 3 + n] = 0
	share1.save("share1.png")
	share2.save("share2.png")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("IMAGE_SHARE_1", help="The image to share 1")
    parser.add_argument("IMAGE_SHARE_2", help="The image to share 2")
    parser.add_argument("IMAGE_SECRET", help="The image to hide")
    args = parser.parse_args()

    encrypt(args.IMAGE_SHARE_1, args.IMAGE_SHARE_2, args.IMAGE_SECRET)