from paddleocr import PaddleOCR
from .local_llm import LocalLLM
# 这边的点"."的意思是，表示这两个在同一目录，否则找不到。

class OCRModule:
    def __init__(self, lang="japan", use_angle_cls=True):
        self.lang = lang
        self.use_angle_cls = use_angle_cls
        self.ocr = PaddleOCR(
            lang=self.lang,
            use_angle_cls=self.use_angle_cls,
        )
        self.llm = LocalLLM()

    def extract_text(self, img_path):
        result = self.ocr.predict(img_path)
        texts = result[0]['rec_texts']
        return texts

    def extract_business_card_info(self, img_path):
        texts = self.extract_text(img_path)
        raw_text = "\n".join(texts)
        # 这行代码的作用就是把这些“list里面的element”用换行符 \n 连接起来，变成一整个大字符串。
        # 也就是说本来texts是list，现在变成了一行一行的文字了。
        prompt = f"""You are a smart business card parsing assistant. 
        Below is the raw OCR text from a business card, 
        each line representing one line on the card. 
        And this is japanese business card, 
        which means the name of company and person's name should be japanese.
        Please extract the following fields and return the result in compact JSON format: name, company, email, address of company, telephone number. 
        If any information is missing, set it as null. Output JSON only, no explanation.
        OCR text:
        {raw_text}
        """
        ai_result = self.llm.call(prompt)
        return ai_result
