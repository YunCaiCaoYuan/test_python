# !!! 未调通
import pytesseract
from PIL import Image
import cv2
import numpy as np

def ocr_tesseract_basic(image_path):
    """
    基础OCR识别
    """
    # 方法1：使用PIL直接打开
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img, lang='chi_sim+eng')
    return text

def ocr_tesseract_with_preprocess(image_path):
    """
    带预处理的OCR识别（提高准确率）
    """
    # 读取图片
    img = cv2.imread(image_path)
    
    # 1. 转为灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 2. 二值化处理
    # 自适应阈值二值化，对光照不均匀的图片效果更好
    binary = cv2.adaptiveThreshold(gray, 255, 
                                  cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                  cv2.THRESH_BINARY, 11, 2)
    
    # 3. 降噪处理
    denoised = cv2.medianBlur(binary, 3)
    
    # 4. 识别
    text = pytesseract.image_to_string(denoised, lang='chi_sim+eng')
    
    return text

# 使用示例
if __name__ == "__main__":
    text = ocr_tesseract_basic('test.jpg')
    print("基础识别结果：")
    print(text)
    
    # 带预处理的识别
    text_processed = ocr_tesseract_with_preprocess('test.jpg')
    print("\n带预处理识别结果：")
    print(text_processed)
