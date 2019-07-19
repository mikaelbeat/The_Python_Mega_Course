import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

image = cv2.imread("photo.jpg")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_image, scaleFactor = 1.05, minNeighbors = 5)

print(faces)

# cv2.imshow("Gray", gray_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# 11:55
