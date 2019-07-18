import cv2, glob2

folder = glob2.glob("Data\*")

for image in folder:
    data = cv2.imread(image, 1)
    resized_image = cv2.resize(data,(100, 100))
    cv2.imwrite(f"{image}", resized_image)

    