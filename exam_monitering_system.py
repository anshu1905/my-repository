import os
import cv2
import dlib
import numpy as np
import time
import face_recognition
import datetime
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D

from pygame import mixer

mixer.init()
sound1 = mixer.Sound('beep-02.wav')
sound2 = mixer.Sound('beep-03.wav')
sound3 = mixer.Sound('pay-attention.wav')
driver_dataset = {'Barack Obama': [0, 0],
                  'Joe Biden': [0, 0],
                  'Shah Rukh Khan': [0, 0],
                  'Anshuman': [0,0],
                  }

class Driver:
    def __init__(self, name):
        self.name = name
        self.time = driver_dataset[self.name][0]

    def updateTime(self, time):
        self.time = time
        driver_dataset[self.name][0] = time


# Load a first sample picture and learn how to recognize it.
obama_image = face_recognition.load_image_file("obama.jpg")
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

# Load a second sample picture and learn how to recognize it.
biden_image = face_recognition.load_image_file("biden.jpg")
biden_face_encoding = face_recognition.face_encodings(biden_image)[0]

# Load a third sample picture and learn how to recognize it
anshuman_image = face_recognition.load_image_file("anshuman.jpg")
anshuman_face_encoding = face_recognition.face_encodings(anshuman_image)[0]

# Load a fourth sample picture and learn how to recognize it 
srk_image = face_recognition.load_image_file("srk.jpg")
srk_face_encoding = face_recognition.face_encodings(srk_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [
    obama_face_encoding,
    biden_face_encoding,
    srk_face_encoding,
    anshuman_face_encoding
]
known_face_names = [
    "Barack Obama",
    "Joe Biden",
    "Shah Rukh Khan",
    "Anshuman"
]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

MoodModel = Sequential()

MoodModel.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(48, 48, 1)))
MoodModel.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
MoodModel.add(MaxPooling2D(pool_size=(2, 2)))
MoodModel.add(Dropout(0.25))

MoodModel.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
MoodModel.add(MaxPooling2D(pool_size=(2, 2)))
MoodModel.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
MoodModel.add(MaxPooling2D(pool_size=(2, 2)))
MoodModel.add(Dropout(0.25))

MoodModel.add(Flatten())
MoodModel.add(Dense(1024, activation='relu'))
MoodModel.add(Dropout(0.5))
MoodModel.add(Dense(7, activation='softmax'))

MoodModel.load_weights('MoodModel.h5')
#This is was the model made for emotion recognition
# prevents openCL usage and unnecessary logging messages
cv2.ocl.setUseOpenCL(False)

cap = cv2.VideoCapture(0)
#turn on the web cam
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1500)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1500)
#set the height and weight of the video window 
emotion_dict = {0: "Angry", 1: "Disgusted", 2: "Fearful", 3: "Happy", 4: "Neutral", 5: "Sad", 6: "Surprised"}

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')


def face_recog(frame):
    global face_locations, face_encodings, face_names, process_this_frame

    result = None

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
                result = name

            face_names.append(name)

    process_this_frame = not process_this_frame

    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    return frame, result


def distance(pt1, pt2):
    return ((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2) ** 0.5


def midpoint(pt1, pt2):
    return int((pt1[0] + pt2[0]) / 2), int((pt1[1] + pt2[1]) / 2)


def rect_to_bb(rect):
    x = rect.left()
    y = rect.top()
    w = rect.right() - x
    h = rect.bottom() - y

    return x, y, w, h
#this is for facial landmarking technique

eyeClosed = 0
driverRecognized = False
driverName = None
noFaceCounter = 0
starTime = 0
score_right = 0
score_left = 0
score_up = 0
score_down = 0

while True:
    
    
    ret, img = cap.read()

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    facemask = np.zeros_like(img_gray)

    eye1mask = np.zeros_like(img_gray)
    eye2mask = np.zeros_like(img_gray)

    eyeFound = False

    if ret:

        if driverRecognized:
            #print the student name

            cv2.putText(img, f'StudentName:{driver1.name}', (10, 70), cv2.FONT_HERSHEY_COMPLEX, 1.5, (255, 204, 0),
                        2)
            driver1.updateTime(time.time() - starTime)
            cv2.putText(img, f'TOD:{str(datetime.timedelta(seconds=(time.time() - starTime), microseconds=0))}',
                        (985, 700),
                        cv2.FONT_HERSHEY_COMPLEX, 1.5, (0, 100, 255), 2)

            faces = detector(img_gray, 0)

            if len(faces) > 0:

                noFaceCounter = 0

                for face in faces:

                    (x, y, w, h) = rect_to_bb(face)

                    # cv2.rectangle(img, (x, y - 50), (x + w, y + h + 10), (255, 0, 0), 2)
                    roi_gray = img_gray[y:y + h, x:x + w]
                    cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray, (48, 48)), -1), 0)
                    MoodPrediction = MoodModel.predict(cropped_img)
                    maxindex = int(np.argmax(MoodPrediction))
                    cv2.putText(img, f'MOOD: {emotion_dict[maxindex]}', (50, 500), cv2.FONT_HERSHEY_COMPLEX, 2,
                                (255, 255, 255), 2)

                    landmarks = predictor(img_gray, face)
                    #print the mood of the driver
                    # unpack the 68 landmark coordinates from the dlib object into a list
                    landmarks_list = []
                    for i in range(0, landmarks.num_parts):
                        landmarks_list.append((landmarks.part(i).x, landmarks.part(i).y))

                        cv2.circle(img, (landmarks.part(i).x, landmarks.part(i).y), 4, (255, 255, 255), -1)

                    points = np.array(landmarks_list, np.int32)

                    _, nose_val = landmarks_list[30]
                    #for detecting up movement of the driver
                    if nose_val < 300:
                        cv2.putText(img, 'UP', (250, 400),
                                    cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255), 2)
                        score_up += 1
                        if score_up > 20:
                            try:
                                sound2.play()
                                score_up = 0
                            except:
                                pass
                    #for detecting down movement of the driver
                    elif nose_val > 480:
                        cv2.putText(img, 'DOWN', (250, 400),
                                    cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255), 2)
                        score_down += 1
                        if score_down > 20:
                            try:
                                sound2.play()
                                score_down = 0
                            except:
                                pass
                    else:
                        cv2.putText(img, 'CENTER', (250, 400),
                                    cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255), 2)
                        score_up = 0
                        score_down = 0

                    # 1-37, 17-46
                    x_1, _ = landmarks_list[0]
                    x_37, _ = landmarks_list[36]
                    side_1_dist = int(x_37 - x_1)

                    x_17, _ = landmarks_list[16]
                    x_46, _ = landmarks_list[45]
                    side_2_dist = int(x_17 - x_46)
                    #now detect the angle of the driver's face for checking left or right position
                    # print(side_1_dist, side_2_dist)
                    #for left head movement
                    if side_1_dist > side_2_dist + 30:
                        cv2.putText(img, 'FACE: LEFT', (50, 300),
                                    cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255), 2)

                        score_right += 1
                        if score_right > 30:
                            try:
                                sound2.play()
                                score_right = 0
                            except:
                                pass

                    #for right head movement
                    elif side_2_dist > side_1_dist + 30:
                        cv2.putText(img, 'FACE: RIGHT', (50, 300),
                                    cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255), 2)
                        score_left += 1
                        if score_left > 30:
                            try:
                                sound2.play()
                                score_left = 0
                            except:
                                pass
                    else:
                        cv2.putText(img, 'FACE: CENTER', (50, 300),
                                    cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255), 2)
                        score_right = 0
                        score_left = 0

                    # faceconvexhull = cv2.convexHull(points)

                    # EYE 1
                    eye1_l = tuple(points[36])
                    eye1_r = tuple(points[39])

                    eye1_top_center = midpoint(points[37], points[38])
                    eye1_bottom_center = midpoint(points[40], points[41])

                    cv2.line(img, eye1_r, eye1_l, (0, 255, 0), 2)

                    cv2.line(img, eye1_top_center, eye1_bottom_center, (0, 255, 0), 2)

                    eye1_ratio = distance(eye1_l, eye1_r) / distance(eye1_top_center, eye1_bottom_center)
                    # horizontal/vertical

                    # EYE 2
                    eye2_l = tuple(points[42])
                    eye2_r = tuple(points[45])

                    eye2_top_center = midpoint(points[43], points[44])
                    eye2_bottom_center = midpoint(points[46], points[47])

                    cv2.line(img, eye2_r, eye2_l, (0, 255, 0), 2)

                    cv2.line(img, eye2_top_center, eye2_bottom_center, (0, 255, 0), 2)

                    eye2_ratio = distance(eye2_l, eye2_r) / distance(eye2_top_center, eye2_bottom_center)
                    #draws a line on the eye for checking the blinking of the eye
                    

                    # cv2.polylines(img, [faceconvexhull], True, (255, 0, 0), 3)

                    # cv2.polylines(img, [points[36:42]], True, (255, 0, 0), 3)
                    # cv2.polylines(img, [points[42:47]], True, (255, 0, 0), 3)

                    # cv2.fillConvexPoly(facemask, faceconvexhull, 255)

                    cv2.fillPoly(eye1mask, [points[36:42]], 255)
                    cv2.fillPoly(eye2mask, [points[42:47]], 255)

                    # face_img = cv2.bitwise_and(img, img, mask=facemask)
                    eye1_img = cv2.bitwise_and(img_gray, img_gray, mask=eye1mask)
                    eye2_img = cv2.bitwise_and(img_gray, img_gray, mask=eye2mask)

                    eye1_min_x = np.min(points[36:42][:, 0])
                    eye1_max_x = np.max(points[36:42][:, 0])
                    eye1_min_y = np.min(points[36:42][:, 1])
                    eye1_max_y = np.max(points[36:42][:, 1])

                    eye2_min_x = np.min(points[36:42][:, 0])
                    eye2_max_x = np.max(points[36:42][:, 0])
                    eye2_min_y = np.min(points[36:42][:, 1])
                    eye2_max_y = np.max(points[36:42][:, 1])

                    eye1 = eye1_img[eye1_min_y:eye1_max_y, eye1_min_x:eye1_max_x]
                    eye2 = eye1_img[eye2_min_y:eye2_max_y, eye2_min_x:eye2_max_x]

                    _, threshold_eye1 = cv2.threshold(eye1, 70, 255, cv2.THRESH_BINARY)
                    threshold_eye1 = cv2.resize(threshold_eye1, None, fx=5, fy=5)
                    h1, w1 = threshold_eye1.shape
                    eye1_left_white = cv2.countNonZero(threshold_eye1[0:h1, 0:int(w1 / 2)])
                    eye1_right_white = cv2.countNonZero(threshold_eye1[0:h1, int(w1 / 2):w1])
                    try:
                        eye1_white_ratio = round(eye1_left_white / eye1_right_white, 2)
                        eyeFound = True
                    except ZeroDivisionError:
                        pass

                    _, threshold_eye2 = cv2.threshold(eye2, 70, 255, cv2.THRESH_BINARY)
                    threshold_eye2 = cv2.resize(threshold_eye2, None, fx=5, fy=5)
                    h2, w2 = threshold_eye2.shape
                    eye2_left_white = cv2.countNonZero(threshold_eye2[0:h2, 0:int(w2 / 2)])
                    eye2_right_white = cv2.countNonZero(threshold_eye2[0:h2, int(w2 / 2):w2])
                    try:
                        eye2_white_ratio = round(eye2_left_white / eye2_right_white, 2)
                        eyeFound = True
                    except ZeroDivisionError:
                        pass

                    if eyeFound:
                        if (eye1_white_ratio + eye2_white_ratio) >= 2.6:
                            cv2.putText(img, 'EYES: LEFT', (50, 200),
                                        cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255), 2)
                            
                        elif 2.6 > (eye1_white_ratio + eye2_white_ratio) > 1:
                            cv2.putText(img, 'EYES: CENTER', (50, 200),
                                        cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255), 2)
                        else:
                            cv2.putText(img, 'EYES: RIGHT', (50, 200),
                                        cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255), 2)
                            

                    try:
                        img2 = cv2.merge((threshold_eye1, threshold_eye1, threshold_eye1))
                        img[0:img2.shape[0], 950:950 + img2.shape[1]] = img2
                        cv2.putText(img, 'RIGHT EYE', (1010, 100),
                                    cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 0), 2)

                        img3 = cv2.merge((threshold_eye2, threshold_eye2, threshold_eye2))
                        img[0:img2.shape[0], 600:600 + img2.shape[1]] = img3
                        cv2.putText(img, 'LEFT EYE', (660, 100),
                                    cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 0), 2)
                    except:
                        cv2.putText(img, 'EYES NOT VISIBLE', (660, 100),
                                    cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 0), 2)
                    #for eye position monitering
            else:
                noFaceCounter += 1
                if noFaceCounter > 100:
                    driverRecognized = False
                    del driver1
        else:
            img, res = face_recog(img)

            if res:
                driverRecognized = True
                driver1 = Driver(res)
                starTime = time.time() - driver1.time
       
        cv2.imshow('Exam Monitering System', img)
    
    key = cv2.waitKey(1)

    if key == ord('q'):
        break
    elif key == ord('a'):
        cv2.imwrite('my_pic.jpg', img)
 
cap.release()
cv2.destroyAllWindows()
