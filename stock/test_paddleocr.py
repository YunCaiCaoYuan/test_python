#！！！安装失败

import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from paddleocr import PaddleOCR


def draw_ocr_result(image, result, font_path=None):
    """
    自定义OCR结果绘制函数
    """
    if isinstance(image, str):
        img = cv2.imread(image)
    elif isinstance(image, Image.Image):
        img = np.array(image)
        if len(img.shape) == 3 and img.shape[2] == 3:
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    else:
        img = image.copy()

    # 遍历所有识别结果
    for line in result:
        for box, (text, confidence) in [line]:
            # 转换为整数坐标
            box = np.array(box, dtype=np.int32)

            # 绘制边界框
            cv2.polylines(img, [box], True, (0, 255, 0), 2)

            # 计算文本位置
            text_position = (box[0][0], box[0][1] - 10)

            # 绘制文本背景
            (text_width, text_height), baseline = cv2.getTextSize(
                f"{text} ({confidence:.2f})",
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5, 1
            )

            cv2.rectangle(
                img,
                (box[0][0], box[0][1] - text_height - 10),
                (box[0][0] + text_width, box[0][1] - 10),
                (0, 255, 0),
                -1
            )

            # 绘制文本
            cv2.putText(
                img,
                f"{text} ({confidence:.2f})",
                text_position,
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 0, 255),
                1,
                cv2.LINE_AA
            )

    return img


# 使用示例

ocr = PaddleOCR(use_angle_cls=True, lang='ch')
result = ocr.ocr('/Users/sunbin/Desktop/111415_6125.png', cls=True)

# 绘制结果
result_img = draw_ocr_result('/Users/sunbin/Desktop/111415_6125.png', result)

# 显示
plt.figure(figsize=(12, 8))
plt.imshow(cv2.cvtColor(result_img, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('OCR识别结果')
plt.show()