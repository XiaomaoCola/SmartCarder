# SmartCarder – Local Smart Business Card Management System (AI-powered)

## Project Overview

SmartCarder is a local smart business card digitization solution for modern enterprises. It integrates cutting-edge computer vision technology with a large language model (LLM) intelligent parsing engine, requiring no expensive hardware or external dependencies. It is lightweight to deploy and extremely secure.

**Core Advantages:**

- **AI business card recognition and structured extraction capabilities comparable to Sansan,** fully localized with no need to upload private data to external clouds
- **No need for dedicated scanners:** just take a photo with your smartphone or upload an image to instantly complete high-precision business card parsing
- **Intelligently extracts key business card information,** automatically structures it and writes it into the database, supporting integration with existing enterprise systems
- **Based on computer vision and generative AI technology,** compatible with most Japanese/international business card templates, with recognition accuracy far exceeding traditional OCR
- **Fully localized process with privacy and security guaranteed,** no need for on-site installation or expensive monthly subscriptions like Sansan

SmartCarder is committed to providing Japanese enterprises and individual users with a **high-end, agile, and customizable enterprise-level business card management experience.**

---

## File Structure

```
SmartCarder/
│
├── Class/
│   ├── extract_text.py    # Core module for OCR + AI
│   └── local_llm.py       # Local LLM request module
│
├── main.py                # Example main program
```

---

## Quick Start

1. Prepare your local large language model API service  
    `local_llm.py` points to `http://localhost:11434/api/generate` by default. Please ensure that this API is available and responding.
2. Place your business card image  
    For example, save it as `C:\Users\xiaomao\Desktop\meishi.jpg`
3. Run the main program

```bash
python main.py
```

**Sample Output:**

```json
{
  "name": "Taro Yamada",
  "company": "Sample Corporation",
  "email": "taro@example.co.jp",
  "address": "1-2-3 Chiyoda, Tokyo",
  "telephone": "03-1234-5678"
}
```

---

## Main Code Explanation

- Class/extract_text.py
    - `OCRModule.extract_text(img_path)`: Uses OCR to extract all text from the image (returns a list)
    - `OCRModule.extract_business_card_info(img_path)`: Directly returns structured JSON information (intelligently extracted using the local large language model)
- Class/local_llm.py
    - `LocalLLM`: Responsible for communication with the local LLM HTTP API
- main.py
    - Example of how to call the modules

---

## Future Expansion Features

SmartCarder is not limited to intelligent business card recognition and management.  
With advanced AI technology combining computer vision and large language model (LLM) algorithms, and with simple configuration or secondary development, it can seamlessly expand to the automated recognition and digitization of various enterprise documents, including but not limited to:

- **Various contracts and agreements** (such as labor contracts, outsourcing agreements, sales contracts, etc.)
- **Invoices, receipts, quotations, purchase orders, and other business documents**
- **Employee IDs, attendance cards, business ledgers**
- **Company rules, internal regulations, approval documents (application forms), various forms**
- **Financial statements, meeting minutes, correspondence, technical white papers, and other documents**

All files can be automatically extracted for key information by AI and registered in the database in real time, helping enterprises realize digital, intelligent, and automated document management.

SmartCarder is committed to helping enterprises achieve true “fully digital offices” and “intelligent document management.”  
From now on, you no longer have to worry about the tedious task of organizing and searching for paper documents, truly achieving—

> **“Scan documents, register data, manage enterprise information assets in one stop.”**
