from Class.extract_text import OCRModule

ocr = OCRModule()
result = ocr.extract_business_card_info("C:\\Users\\LuluL\\Desktop\\SharedFiles\\meishi.jpg")
print(result)