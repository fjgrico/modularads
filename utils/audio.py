import os
from elevenlabs.client import ElevenLabs

def generar_audios(modulos):
    client = ElevenLabs(api_key=os.getenv("ELEVEN_API_KEY"))

    os.makedirs("audios", exist_ok=True)
    textos = modulos["hooks"].split("\n")[:3] + modulos["ctas"].split("\n")[:1]

    for i, texto in enumerate(textos):
        audio = client.generate(
            text=texto,
            voice="Antoni",
            model="eleven_monolingual_v1"
        )
        with open(f"audios/bloque_{i+1}.mp3", "wb") as f:
            f.write(audio.to_bytes())
