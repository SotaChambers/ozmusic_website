import cv2

ref_img = cv2.imread("images/link_2.jpeg")
target_img = cv2.imread("images/link_4.jpeg")

target_img = cv2.resize(target_img, (ref_img.shape[1], ref_img.shape[0]))

cv2.imwrite("images/link_test.jpeg", target_img)
