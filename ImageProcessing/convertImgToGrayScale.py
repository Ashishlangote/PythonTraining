import cv2

color = cv2.imread('galaxy.jpg', 0)
cv2.imwrite('galaxy-gray.jpg', color)
