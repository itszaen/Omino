#!/usr/bin/env python3

import face_recognition
import sys
from PIL import Image, ImageFont, ImageDraw, ImageEnhance

input = sys.argv[1]


def find_face():
    image = face_recognition.load_image_file(input)
    face_locations = face_recognition.face_locations(image)

    source_img = Image.open(input).convert("RGB")
    draw = ImageDraw.Draw(source_img)

    for face_location in face_locations:
        top, right, bottom, left = face_location
        print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top,left,bottom,right))
        draw.rectangle(((left,top),(right,bottom)),outline=(256,256,256))
        draw.text((right+5,bottom+5),"www")

    source_img.save("2.jpg","JPEG")

if __name__ == '__main__':
    if input is not None:
        find_face()
    else:
        print('No input file. Aborting.')
