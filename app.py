import os
import json
from ollama import Client

class HustleGuardAgent:
    def __init__(self):
        print("[*] Connecting to Local Ollama Inference Engine (Gemma 2)...")
        self.local_client = Client(host='http://localhost:11434')
        self.model_name = "gemma2:2b"
        
        self.system_instruction = (
            "You are HustleGuard, an elite AI assistant for freelancers and side-hustlers. "
            "Your job is to generate highly professional project proposals or legal freelance contracts "
            "based on the user specifications. Keep inputs highly structured and legally clear."
        )

    def generate_hustle_asset(self, asset_type: str, details: str) -> str:
        """تشغيل استدلال محلي 100% بدون إنترنت لتوليد العقد أو العرض"""
        prompt = f"Generate a professional {asset_type} based on these client details: {details}"
        try:
            response = self.local_client.chat(
                model=self.model_name,
                messages=[
                    {"role": "system", "content": self.system_instruction},
                    {"role": "user", "content": prompt}
                ]
            )
            return response['message']['content']
        except Exception as e:
            print(f"[!] Ollama Connection Error: {e}")
            return "Error: Could not connect to local inference core."

    def speak_financial_summary(self, text_output: str):
        """نظام النطق الصوتي المدمج محلياً لقراءة البنود المالية والملخص"""
        print(f"\n🔊 Streaming crucial milestones to side-hustler headphones...")
        
        clean_text = text_output.replace("*", "").replace("\n", " ").replace("'", "").replace('"', "")
        
        summary_sentences = ". ".join(clean_text.split(". ")[:2])
        
        try:
            import win32com.client
            speaker = win32com.client.Dispatch("SAPI.SpVoice")
            speaker.Speak(summary_sentences)
        except Exception:
            os.system(f'powershell -Command "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{summary_sentences}\')"')

    def run_freelance_pipeline(self, asset_type: str, specifications: str):
        print(f"\n🚀 [Processing {asset_type} Request]...")
        output = self.generate_hustle_asset(asset_type, specifications)
        print(f"\n🧠 [Gemma 2 Generation Output]:\n{output}")
        self.speak_financial_summary(output)

if __name__ == "__main__":
    print("==================================================")
    print("💼 HustleGuard: Local AI Side-Hustle Engine Active 💼")
    print("==================================================")
    
    agent = HustleGuardAgent()
    
    freelance_specs = "Project: E-commerce Website Development. Client Name: Acme Corp. Budget: $1500 USD. Deadline: 2 weeks. Milestones: 50% upfront, 50% on completion."
    agent.run_freelance_pipeline("Freelance Legal Contract", freelance_specs)
