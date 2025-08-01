import cv2
import dlib
import pyttsx3
from scipy.spatial import distance
import time
from picamera2 import Picamera2
import pygame

pygame.mixer.init()
sound_file = '/home/pi/wake_up.wav'
pygame.mixer.music.load(sound_file)
pygame.mixer.music.set_volume(0.5)

engine = pyttsx3.init()
face_detector = dlib.get_frontal_face_detector()
camera = Picamera2()
camera.configure(camera.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
camera.start()
time.sleep(0.1)

dlib_facelandmark = dlib.shape_predictor('/home/pi/shape_predictor_68_face_landmarks.dat')

def detect_eye(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    aspect_ratio = (A + B) / (2.0 * C)
    return aspect_ratio

eyes_closed = False
closed_eye_timer_start = 0
eye_closure_threshold = 0.25
max_closed_duration = 0.55

while True:
    cam = camera.capture_array()
    grey = cv2.cvtColor(cam, cv2.COLOR_BGR2GRAY)
    faces = face_detector(grey)

    for face in faces:
        landmarks = dlib_facelandmark(grey, face)
        left_eye, right_eye = [], []

        for n in range(42, 48):  # Right Eye
            x, y = landmarks.part(n).x, landmarks.part(n).y
            right_eye.append((x, y))

        for n in range(36, 42):  # Left Eye
            x, y = landmarks.part(n).x, landmarks.part(n).y
            left_eye.append((x, y))

        left = detect_eye(left_eye)
        right = detect_eye(right_eye)
        eye_ratio = (left + right) / 2.0

        if eye_ratio < eye_closure_threshold:
            if not eyes_closed:
                closed_eye_timer_start = time.time()
                eyes_closed = True
        else:
            eyes_closed = False

        if eyes_closed:
            elapsed = time.time() - closed_eye_timer_start
            cv2.putText(cam, f"Sleeping - Eyes closed for {int(elapsed)}s", (50, 100),
                        cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            if elapsed > max_closed_duration:
                cv2.putText(cam, "ALERT! WAKE UP!", (50, 450),
                            cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
                pygame.mixer.music.play()
                time.sleep(5)
                pygame.mixer.music.stop()
                engine.say("Alert! Wake up!")
                engine.runAndWait()

    cv2.imshow("Eye Tracker", cam)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
