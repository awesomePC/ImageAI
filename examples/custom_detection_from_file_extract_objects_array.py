from imageai.Detection.Custom import CustomObjectDetection
import cv2


detector = CustomObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath("hololens-ex-60--loss-2.76.h5") # download via https://github.com/OlafenwaMoses/ImageAI/releases/download/essential-v4/hololens-ex-60--loss-2.76.h5
detector.setJsonPath("detection_config.json") # download via https://github.com/OlafenwaMoses/ImageAI/releases/download/essential-v4/detection_config.json
detector.loadModel()
detected_image, detections, extracted_objects  = detector.detectObjectsFromImage(input_image="holo2.jpg", extract_detected_objects=True, output_type="array")


for eachObject in detections:
    print(eachObject["name"], " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"])

cv2.imshow("Main Image", detected_image)
count = 0
for img in extracted_objects:
    count += 1

    cv2.imshow("Window" + str(count), img)

cv2.waitKey()
cv2.destroyAllWindows()


"""
SAMPLE RESULT

hololens  :  39.69653248786926  :  [611, 74, 751, 154]
hololens  :  87.6643180847168  :  [23, 46, 90, 79]
hololens  :  89.25175070762634  :  [191, 66, 243, 95]
hololens  :  64.49641585350037  :  [437, 81, 514, 133]
hololens  :  91.78624749183655  :  [380, 113, 423, 138]

"""