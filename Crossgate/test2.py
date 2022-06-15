import pytesseract
from PIL import Image
# 读取图片
im = Image.open("skill.png")
# 识别文字
string = pytesseract.image_to_string(im, lang="chi_sim").encode('gb18030').decode('big5')
print(string)