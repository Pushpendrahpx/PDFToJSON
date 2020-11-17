from pdf2image import convert_from_path 
# Import modules
from PIL import Image
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
 
# Store Pdf with convert_from_path function 
images = convert_from_path('syllabus.pdf') 
i = 0
for img in images: 
    i = i+1
    img.save('out/output'+str(i)+'.jpg', 'JPEG')
print("Images Created !!")
for i in range(1,73):
    print(i)
    image = Image.open('out/output'+str(i)+'.jpg')
    if(image):
        image_to_text = pytesseract.image_to_string(image, lang='eng')
        file1 = open("Text/myfile"+str(i)+".txt","w") 
        file1.write(image_to_text+" \n") 
        file1.close()
        print("Text Converted "+str(i))
