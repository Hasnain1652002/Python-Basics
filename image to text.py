# Open the uploaded image
img_path2 = "/mnt/data/paper2 .jpg"
img2 = Image.open(img_path2)

# Use OCR to extract text from the image
text2 = pytesseract.image_to_string(img2)
text2
