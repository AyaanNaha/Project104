import cv2

img = cv2.imread("solar-system.jpg")
cv2.imshow("solar-system.jpg", img)

cv2.putText(img, "Sun", (20, 300), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255))
cv2.putText(img, "Mercury", (120, 250), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "Venus", (200, 180), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "Earth", (300, 270), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "Mars", (380, 180), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "Jupiter", (480, 350), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "Saturn", (750, 100), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "Uranus", (900, 160), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "Neptune", (1100, 160), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))



cv2.imwrite("Solar_systemwithname.jpg", img)
output = cv2.imread("Solar_systemwithname.jpg")

cv2.imshow("Solar_systemwithname.jpg", output)

cv2.waitKey(0)