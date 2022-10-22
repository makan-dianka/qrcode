import pyqrcode
import png
from pyqrcode import QRCode

link = "www.makandianka.org"
qr = pyqrcode.create(link)
qr.svg("qrcodes/qrcode1.svg", scale=8)
qr.png("qrcodes/qrcode2.png", scale=6)