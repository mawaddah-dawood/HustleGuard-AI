import os
from ollama import Client

class EcoEchoOfflineAgent:
    def __init__(self):
        print("[*] Connecting to Local Ollama Inference Engine...")
        self.local_client = Client(host='http://localhost:11434')
        self.model_name = "gemma2:2b" 
        
        self.system_instruction = (
            "You are EcoEcho, an offline wilderness survival AI assistant. "
            "Provide immediate, short, step-by-step emergency advice. "
            "Keep answers very brief, under 3 sentences."
        )

    def get_local_ai_response(self, hiker_incident: str) -> str:
        """تشغيل استدلال محلي 100% بدون إنترنت عبر Gemma"""
        try:
            response = self.local_client.chat(
                model=self.model_name,
                messages=[
                    {"role": "system", "content": self.system_instruction},
                    {"role": "user", "content": hiker_incident}
                ]
            )
            return response['message']['content']
        except Exception as e:
            return "Emergency active. Keep calm and stay near shelter."

    def speak_locally(self, text_advice: str):
        """توليد صوت ينطق محلياً 100% باستخدام ميزات الويندوز المدمجة وبدون إنترنت وبدون أخطاء"""
        print(f"🔊 Speaking instructions text-to-speech locally...")
        
        clean_text = text_advice.replace("*", "").replace("\n", " ").replace("'", "").replace('"', "")
        
        try:
            import win32com.client
            speaker = win32com.client.Dispatch("SAPI.SpVoice")
            speaker.Speak(clean_text)
        except Exception:
            os.system(f'powershell -Command "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{clean_text}\')"')

    def handle_trail_emergency(self, incident: str):
        print(f"\n🚀 [Incident Received]: {incident}")
        ai_response = self.get_local_ai_response(incident)
        print(f"\n🧠 [Local AI Evaluation]:\n{ai_response}")
        self.speak_locally(ai_response)

if __name__ == "__main__":
    print("==================================================")
    print("🌲 EcoEcho: 100% Offline AI Voice Hacking Active 🌲")
    print("==================================================")
    
    companion = EcoEchoOfflineAgent()
    companion.handle_trail_emergency("I am deep in the woods and my friend just got bitten by a snake!")
