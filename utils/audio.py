import os
from elevenlabs.client import ElevenLabs

def generar_audios(modulos):
    client = ElevenLabs(api_key=os.getenv("ELEVEN_API_KEY"))
    os.makedirs("audios", exist_ok=True)
    textos = modulos["hooks"].split("\n")[:3] + modulos["ctas"].split("\n")[:1]

    for i, texto in enumerate(textos):
        audio_generator = client.generate(
            text=texto,
            voice="cgSgspJ2msm6clMCkdW9",  # Voz personalizada
            model="eleven_monolingual_v1",
            stream=False  # No usamos el streaming ahora
        )

        with open(f"audios/bloque_{i+1}.mp3", "wb") as f:
            # Si el audio es un generador, recogemos y escribimos los bytes
            for chunk in audio_generator:
                if isinstance(chunk, bytes):
                    f.write(chunk)
                else:
                    raise TypeError(f"El trozo de audio no es de tipo bytes, sino {type(chunk)}")
