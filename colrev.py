#!/usr/bin/python3
from PIL import Image
from sys import argv

def help():
	print(f'usage: {argv[0]} <file>')
	exit()

def rescale(t,min,max):
	assert len(t) == len(min) == len(max)
	out = []
	for i in range(len(t)):
		out.append (int( ( (t[i]-min[i]) / (max[i]-min[i]) ) * 255 * Contrast_overflow) )
	if len(t)==4:
		out[-1]=255
	out =  tuple(out)
	return out

def get_borders(input):
	all_input  = []
	for x in range(width):
		for y in range(height):
			all_input.append(image_pixels[x,y])
	min_input  = min(all_input)
	max_input  = max(all_input)
	return min_input, max_input

if __name__=='__main__':	
	input_file = argv[1] if len(argv) > 1 else ''
	if not input_file: raise IOError ('No input file: please use command line arguments')
	if input_file=='-h': help()

	image  = Image.open(input_file)
	image_pixels  = image.load()
	width, height = image.size

	Contrast_overflow = 1

	min_input, max_input = get_borders(image)

	for x in range(width):
		for y in range(height):
			pixel = image_pixels[x,y]
			pixel = rescale (pixel, min_input, max_input)
			image_pixels[x,y] = pixel
	output_file = input_file.replace('.','_adjusted.') if '.' in input_file else input_file+'_adjusted'
	image.save(output_file)
