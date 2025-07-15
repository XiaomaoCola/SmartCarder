from paddleocr import PaddleOCR
from local_llm import LocalLLM
class OCRModule:
    def __init__(self, lang="japan", use_angle_cls=True):
        self.lang = lang
        self.use_angle_cls = use_angle_cls
        self.ocr = PaddleOCR(
            lang=self.lang,
            use_angle_cls=self.use_angle_cls,
        )

    def extract_text(self, img_path):
        result = self.ocr.predict(img_path)
        texts = result[0]['rec_texts']
        return texts

    def extract_business_card_info(self, img_path):
        texts = self.extract_text(img_path)
        raw_text = "\n".join(texts)
        prompt = f"""You are a smart business card parsing assistant. Below is the raw OCR text from a business card, each line representing one line on the card. 
        Please extract the following fields and return the result in compact JSON format: name, company, email. If any information is missing, set it as null. Output JSON only, no explanation.
        OCR text:
        {raw_text}
        """
        ai_result = self.llm.call(prompt)
        return ai_result
