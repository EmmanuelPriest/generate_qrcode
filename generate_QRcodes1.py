#!/usr/bin/python3

'''Defines the generation of QR codes'''
import pyqrcode
from pyqrcode import QRCode


# string input for the QR code
message = "What'sYourColour"

# generate QR code
QR_code = pyqrcode.create(message)

# create and save the svg(Scalar Vector Graphics) file
QR_code.svg("QR_code.svg", scale=8)
