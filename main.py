from PIL import Image
from pytesseract import pytesseract

#define la ruta al archivo tessaract.exe
ruta_tessaract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#Define ruta a la imagen
ruta_czech    = "img2/czech.png"
ruta_arabic   = "img2/arabic.png"
ruta_japanese = "img2/japanese.png"
#ruta_imagen = 'img2/japanese.png'

#Apuntar tessaract_cmd a la ruta de tessaract.exe
pytesseract.tesseract_cmd = ruta_tessaract

#Abre la imagen con PIL *Python Imaging Library* o "Pillow"
#img = Image.open(ruta_imagen)
imagen_czech    = Image.open(ruta_czech)
imagen_arabic   = Image.open(ruta_arabic)
imagen_japanese = Image.open(ruta_japanese)

# List of available languages
print(pytesseract.get_languages(config=''))

#Extrae el texto de la imagen.
#text = pytesseract.image_to_string(img, lang='jpn')

print()
print(pytesseract.image_to_string(imagen_czech, lang="ces"))
print(pytesseract.image_to_string(imagen_arabic, lang="ara"))
print(pytesseract.image_to_string(imagen_japanese, lang="jpn"))

#print(text)