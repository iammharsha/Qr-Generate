import uuid
import qrcode
import string
from PIL import Image

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=10,
    border=4,
)

def randgen():
	u=str(uuid.uuid4())
	x=u[:6]
	x=x.replace("-","")
	return x
for i in range(0,1):
	y=randgen()
	qr.add_data(y)
	qr.make(fit=True)
	img = qr.make_image()
	img.save("/home/ubuntu/Qrcode/"+y+".png")
	qr.clear()
	

