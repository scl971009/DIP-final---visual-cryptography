import argparse
import random

from PIL import Image

seq = [ 1, 2, 3, 4, 5, 6, 7, 8, 9]
randomseq= [ 1 ,   2,    3,    4,    5]

def binary_convert(n):
	binary_1=1
	binary = [x for x in seq if ((n>>(x-1))&binary_1 )]

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
	phototype="RGB"
	original_share1 = Image.open(filename1)
	original_share1 = original_share1.convert(phototype)
	original_s1_pixels = original_share1.load()

	original_share2 = Image.open(filename2)
	original_share2 = original_share2.convert(phototype)
	original_s2_pixels = original_share2.load()


	secret = Image.open(filename_s)
	secret = secret.convert(phototype)
	se_pixels = secret.load()
	

	length=original_share1.size[0]
	width=original_share1.size[1]
	share1 = Image.new(phototype, (length * 3, width * 3))
	s1_pixels = share1.load()
	#s1_pixels[0,0]=(1,2,3,255)
	#print(s1_pixels[0,0])
	#return
	share2 = Image.new(phototype, (length * 3, width * 3))
	s2_pixels = share2.load()

	

	for i in range(length):
		for j in range(width):
			

			s1=[0,0,0]
			s2=[0,0,0]
			list1=[[],[],[]]
			list2=[[],[],[]]
			
			for r in range(3):
				s=binary_convert(se_pixels[i,j][r])
				s_inv=[x for x in seq if ((x not in s ) and (x !=9))]
				if len(s_inv)/2 >=1:
					list1[r]=get_random(s_inv,int(len(s_inv)/2))

				list2[r]=[x for x in s_inv if x not in list1[r]]
				for x in s:
					list1[r].append(x)
					list2[r].append(x)


			for k in seq:
				m,n=setk(k)
					#print(se_pixels[i,j][r],s)
				#v=get_random(randomseq,1)

				for r in range(3):
					if k in list1[r]:
						s1[r] = original_s1_pixels[i,j][r]
					else :
						s1[r] = original_s1_pixels[i,j][r]-1
						if s1[r]<0:
							s1[r]=2
					if k in list2[r]:
						s2[r] = original_s2_pixels[i,j][r]
					else :
						s2[r] = original_s2_pixels[i,j][r]-1
						if s2[r]<0:
							s2[r]=2



				s1_pixels[ i*3 + m , j*3 + n ]=(s1[0],s1[1],s1[2])
				s2_pixels[ i*3 + m , j*3 + n ]=(s2[0],s2[1],s2[2])
				#s3_pixels[ i*3 + m , j*3 + n ]=(s3[0],s3[1],s3[2])
				#print("s1=",s1_pixels[ i*3 + m , j*3 + n ])
				#print("s2=",s2_pixels[ i*3 + m , j*3 + n ])
				#print("s3=",s3_pixels[ i*3 + m , j*3 + n ])
			

							
			
	share1.save("share1.png")
	share2.save("share2.png")
	#share3.save("share3_RGB.png")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("IMAGE_SHARE_1", help="The image to share 1")
    parser.add_argument("IMAGE_SHARE_2", help="The image to share 2")
    #parser.add_argument("IMAGE_SHARE_3", help="The image to share 3")
    parser.add_argument("IMAGE_SECRET", help="The image to hide")
    args = parser.parse_args()

    encrypt(args.IMAGE_SHARE_1, args.IMAGE_SHARE_2,args.IMAGE_SECRET)