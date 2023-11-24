from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
img = Image.open('test.jfif')
#blackAndWhite = img.convert("L") # перевод изображения в чб
#blackAndWhite.show()
#поиск текста на изображении
str = pytesseract.image_to_string(img, lang='rus')
print(str)