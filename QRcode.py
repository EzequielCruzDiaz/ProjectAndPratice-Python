import pyqrcode
import png
from pyqrcode import QRCode

s = "https://www.pinterest.com/pin/633387440103737/"

url = pyqrcode.create(s)
url.svg ("Myqr.svg", scale = 8)

url.png("Myqr.png", scale = 6)