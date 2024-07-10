from PIL import Image
import pytesseract

# Defina o caminho para o executável do Tesseract se não estiver no PATH do sistema
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Carregue a imagem
image = Image.open("empresa-texto.jpg")

# Extraia o texto da imagem
extracted_text = pytesseract.image_to_string(image)

# Imprima o texto extraído
print(extracted_text)
