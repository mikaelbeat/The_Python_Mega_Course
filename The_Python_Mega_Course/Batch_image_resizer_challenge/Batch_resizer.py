import cv2, glob2

folder = glob2.glob("Data\*")

for image in folder:
    data = cv2.imread(image, 1)
    resized_image = cv2.resize(data,(100, 100))
    print(f"\nResizing image {image}...")
    image = image.rsplit(".",1)[0]
    cv2.imwrite(f"{image}_resized.jpg", resized_image)
    
print("\nResized all images in folder!")