from PIL import Image
import os

path="/home/ubuntu/Qrcode"

def merge_images(image1, file2,count2,result):
    """Merge two images into one, displayed side by side
    :param file1: path to first image file
    :param file2: path to second image file
    :return: the merged Image object
    """
    #image1 = Image.open(path+file1)
    image2 = Image.open(path+"/"+file2)

    (width1, height1) = image1.size
    (width2, height2) = image2.size
    if count2%4 == 1:
  	result_width = max(width1,width2)
  	result_height = height1+height2
    	#result = Image.new('RGB', (result_width, result_height))
	result.paste(im=image1, box=(0, 0))
    	result.paste(im=image2, box=(0, heigth1))
    else:
	result_width = width1 + width2
  	result_height = max(height1, height2)
    	#result = Image.new('RGB', (result_width, result_height))
	result.paste(im=image1, box=(0, 0))
    	result.paste(im=image2, box=(width1, 0))
    return result


count=1
count1=0
i=1
img=Image.open("/home/ubuntu/Qrcode/0a0bba.png")
img=thumbnail((cm(200),cm(200))
#result=Image.new('RGB', (3508, 4961))
for file in os.listdir(path):
   if file.endswith(".png"):
	if file=="0a0bba.png":
		continue
        print(file)
	img=merge_images(img,file,count,result)
	count+=1
	if count==32:	
		img.save("/home/ubuntu/Images/image"+str(count1)+".png")
		result=Image.new('RGB', (3508, 4961))
		count1+=1
		count=1
		img=None




