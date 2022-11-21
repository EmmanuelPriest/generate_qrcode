#!/usr/bin/python3

'''Defines QRcode generation'''
import pyqrcode


message = input("Enter the message to generate QR code: ")

# Creating a pyqrcode object by calling create() method
qr_code = pyqrcode.create(message)

# calling the svg() method of the qr_code object
# creates the file named qr_code.svg in svg(Scalar Vector Graphic) format
# the scale argument sets how large to draw a single image
qr_code.svg("qr_code.svg", scale=10)
