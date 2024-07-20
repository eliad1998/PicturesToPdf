#https://stackoverflow.com/questions/30227466/combine-several-images-horizontally-with-python
# pip install fpdf
# pip install Pillow --user
from os import listdir,chdir
from fpdf import FPDF
from PIL import Image

COMBINED_NAME = 'combined_{0}.jpg'


def images_to_pdf(combined_list):
	pdf = FPDF()

	pdf.add_page()
	for image in combined_list:
	    pdf.image(image,x,y,w,h)

	pdf.output("yourfile.pdf", "F")


def image_combine(image_list, image_num):

	imagelist = listdir(path) # get list of all images
	imagelist.reverse()
	images = [Image.open(x) for x in imagelist]

	widths, heights = zip(*(i.size for i in images))

	heights = [height + 500 for height in heights]

	total_width = sum(widths)
	max_height = max(heights)

	new_im = Image.new('RGB', (total_width, max_height))

	x_offset = 0
	for im in images:
	  new_im.paste(im, (x_offset,0))
	  x_offset += im.size[0]

	new_im.save(COMBINED_NAME.format(image_num))

def main():
	path = r"E:\\no_sep_20" # get the path of images
	chdir(path)

	imagelist = listdir(path) # get list of all images
*

