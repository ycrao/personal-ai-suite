from cnocr import CnOcr

img_fp = './sample.jpg'
ocr = CnOcr()  # 所有参数都使用默认值
out = ocr.ocr(img_fp)
print(out)
