#!/usr/bin/env python3

import face_recognition
input = sys.argv[1]


def find_face():
    image = face_recognition.load_image_file(input)
    face_locations = face_recognition.face_locations(image)

if __name__ == '__main__':
    if input is not null:
        find_face()
    else:
        print('No input file. Aborting.')
