#!/usr/bin/env python3

import face_recognition

def identify_faces():
    input_known = sys.argv[1]
    input_unknown = sys.argv[2]

    known_image = face_recognition.load_image_file(input_known)
    unknown_image =face_recognition.load_image_file(input_unknown)

    known_encoding = face_recognition.face_encodings(known_image)[0]
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

    results = face_recognition.compare_faces([known_encoding], unknown_encoding)

    print(results)

if __name__ == '__main__':
    if input[1] is null or input[2] is null:
        identify_faces()
    else:
        print('No input file. Aborting.')
