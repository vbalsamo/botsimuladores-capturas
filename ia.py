import cv2
def is_face(img):

    # Load the cascades
    face_cascade_frontal = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
    face_cascade_alt2 = cv2.CascadeClassifier('cascades/haarcascade_frontalface_alt2.xml')
    face_cascade_alt = cv2.CascadeClassifier('cascades/haarcascade_frontalface_alt.xml')

    # Load the image and convert it to grayscale
    image = cv2.imread(img)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces using the four cascades
    faces_frontal = face_cascade_frontal.detectMultiScale(gray, 1.3, 5)
    faces_alt2 = face_cascade_alt2.detectMultiScale(gray, 1.3, 5)
    faces_alt = face_cascade_alt.detectMultiScale(gray, 1.3, 5)

    contadorCaras = 0

    if len(faces_frontal)>0:
        contadorCaras = contadorCaras + 1
    if len(faces_alt)>0:
        contadorCaras = contadorCaras + 1
    if len(faces_alt2)>0:
        contadorCaras = contadorCaras + 1

    if contadorCaras > 1 and contadorCaras <12:
        return True

    else:
        return False

def is_profile_face(img):

    # Load the cascades
    face_cascade_profile = cv2.CascadeClassifier('cascades/haarcascade_profileface.xml')
    
    # Load the image and convert it to grayscale
    image = cv2.imread(img)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces using the four cascades
    faces_profile = face_cascade_profile.detectMultiScale(gray, 1.3, 5)

    if len(faces_profile) > 0:
        for (x, y, w, h) in faces_profile:
            if(w > 200 and h > 200):
                return True
            else:
                return False
    else:
        return False