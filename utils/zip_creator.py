import zipfile
import os

def crear_zip_entrega(modulos):
    output = "entrega_modular.zip"
    with zipfile.ZipFile(output, "w") as zipf:
        for i in range(3):
            mp3 = f"audios/bloque_{i+1}.mp3"
            if os.path.exists(mp3):
                zipf.write(mp3)
        zipf.writestr("hooks.txt", modulos["hooks"])
        zipf.writestr("cuerpos.txt", modulos["cuerpos"])
        zipf.writestr("ctas.txt", modulos["ctas"])
    return output