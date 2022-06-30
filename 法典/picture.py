# 导入需要的包
import cv2

# 载入图像并显示
image = cv2.imread("1.jpg")

# 保持图片的宽高等比例缩放，以保证图片显示不变形
# 计算新图片相对于旧图片的比例
r = 1000.0/image.shape[1]
dim = (1000, int(image.shape[0]*r))

# 执行图片缩放，并显示
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("resized", resized)
cv2.waitKey(0)
