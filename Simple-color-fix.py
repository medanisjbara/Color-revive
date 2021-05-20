from PIL import Image

input  = Image.open('input.png')
input_pixels  = input.load()
width, height = input.size

RBG = 1.7

def rescale(t,min,max):
	assert len(t)==len(min)==len(max)
	out = []
	for i in range(len(t)):
		out.append(int(((t[i]-min[i])/max[i])*255*RBG))
	if len(t)==4:
		out[-1]=255
	out =  tuple(out)
	return out

def minus(t1,t2):
	assert len(t1)==len(t2)
	out = []
	for i in range(len(t1)):
		color = t1[i]-t2[i]
		out.append(color)
	if len(t1)==4:
		out[3]=255
	out =  tuple(out)
	return out

def get_borders(input):
	all_input  = []
	for x in range(width):
		for y in range(height):
			all_input.append(input_pixels[x,y])
	min_input  = min(all_input)
	max_input  = max(all_input)
	return min_input, max_input

min_input, max_input = get_borders(input)

for x in range(width):
	for y in range(height):
		pixel = input_pixels[x,y]
		pixel = rescale(pixel,min_input,max_input)
		input_pixels[x,y]=pixel
input.show()
