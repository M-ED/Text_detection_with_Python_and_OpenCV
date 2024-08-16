## Read Image
import cv2
import easyocr
import matplotlib.pyplot as plt

## Instance text detector
img_path = r'C:\Users\Fame\Desktop\Projects_2024\Computer_Vision_Beginner_Projects\Text_detection_with_Python_and_Opencv _OCR_using_EasyOCR\test1.png'
img=cv2.imread(img_path)
## img=cv2.imshow(img)

## Detect text on image
reader=easyocr.Reader(['en'], gpu=False)

text_=reader.readtext(img)

threshold = 0.25
## draw bbox or text
for t in text_:
    print(t)

    bbox, text, score=t
    if score>threshold:        
        cv2.rectangle(img, bbox[0], bbox[2], (0, 255, 0), 5)
        cv2.putText(img, text, bbox[0], cv2.FONT_HERSHEY_COMPLEX, 0.65, (255, 0, 0), 2)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

plt.show()
    

    
## Draw bbox and text