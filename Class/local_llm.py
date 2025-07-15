import requests

class LocalLLM:
    def __init__(self, url="http://localhost:11434/api/generate", model="gemma3:4b", timeout=30):
        self.url = url
        self.model = model
        self.timeout = timeout

    def call(self, prompt):
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }
        try:
            response = requests.post(self.url, json=payload, timeout=self.timeout)
            result = response.json()
            return result.get("response", "")
        except Exception as e:
            print(f"[!] LLM接口调用异常: {e}")
            return ""