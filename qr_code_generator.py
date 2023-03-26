
import qrcode

    # pip install qrcode
    # pip install image
    # pip install gradio
qr=qrcode.QRCode(version=15,border=5,box_size=10,error_correction=qrcode.constants.ERROR_CORRECT_M)
data="https://byjus.com/maths/unit-vector/"
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black",back_color="White")
img.save("bjus.png")