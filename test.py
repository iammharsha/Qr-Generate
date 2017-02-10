import uuid
import qrcode
import string
from PIL import Image
import urllib


path="/home/ubuntu/Qrcode/"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=10,
    border=4,
)

def randgen():
	u=str(uuid.uuid4())
	x=u[:5]
	x=x.replace("-","")
	x=x.lower()
	return x
for i in range(0,1):
	y=randgen()
	z="K"+y
	print z
	#image=Image.save(http://qrickit.com/api/qr?d=&addtext=&qrsize=150&t=p&e=m)	
	image = urllib.URLopener()
	image.retrieve("http://qrickit.com/api/qr?d="+z+"&addtext="+z+"&qrsize=150&t=p&e=m",path+z+".png")
	#qr.add_data(y)
	#qr.make(fit=True)
	#img = qr.make_image()
	#img.save("/home/ubuntu/Qrcode/K"+y+".png")
	#qr.clear()
	

