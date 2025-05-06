from elevenlabs import generate, save, set_api_key
import os

set_api_key(os.getenv("ELEVEN_API_KEY"))

def generar_audios(modulos):
    os.makedirs("audios", exist_ok=True)
    textos = modulos["hooks"].split("\n")[:3] + modulos["ctas"].split("\n")[:1]  # demo
    for i, texto in enumerate(textos):
        audio = generate(text=texto, voice="Antonio", model="eleven_monolingual_v1")
        save(audio, f"audios/bloque_{i+1}.mp3")