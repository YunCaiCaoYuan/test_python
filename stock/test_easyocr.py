### ok
# 使用示例
import easyocr
import cv2

# 创建reader，第一次会自动下载模型
reader = easyocr.Reader(['ch_sim', 'en'])  # 中文简体+英文

# 识别图片
result = reader.readtext('/Users/sunbin/Desktop/111415_6125.png')

# 输出结果
for detection in result:
    print(f"文本: {detection[1]}, 置信度: {detection[2]:.2f}")

# 获取所有文本
text = ' '.join([item[1] for item in result])
print(f"全部文本: {text}")
